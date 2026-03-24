import bpy
import random
import string
from bpy.app.handlers import persistent

# Mapping between Blender object types, preferences, and bpy.data collections
greasepencil_type = 'GREASEPENCIL'if bpy.app.version >= (4, 3, 0) else 'GPENCIL'
greasepencil_col = "grease_pencils_v3" if bpy.app.version >= (4, 3, 0) else "grease_pencils"

OBJECT_TYPE_MAPPING = {
    ('MESH', None): ("sync_mesh", "meshes"),
    ('CURVE', None): ("sync_curve", "curves"),
    ('SURFACE', None): ("sync_surface", "curves"),
    ('META', None): ("sync_meta", "metaballs"),
    ('FONT', None): ("sync_text", "curves"),
    ('CURVES', None): ("sync_hair", "hair_curves"),
    ('POINTCLOUD', None): ("sync_pointcloud", "pointclouds"),
    ('VOLUME', None): ("sync_volume", "volumes"),
    (greasepencil_type, None): ("sync_greasepencil", greasepencil_col),
    ('ARMATURE', None): ("sync_armature", "armatures"),
    ('LATTICE', None): ("sync_lattice", "lattices"),
    ('EMPTY', 'IMAGE'): ("sync_image", "images"),
    ('LIGHT', None): ("sync_light", "lights"),
    ('LIGHT_PROBE', None): ("sync_lightprobe", "lightprobes"),
    ('CAMERA', None): ("sync_camera", "cameras"),
    ('SPEAKER', None): ("sync_speaker", "speakers"),
}

# Stips "sync_" from mappings to be used in get_per_object_affixes()
TYPE_TO_AFFIX = {
    key: value[0].replace("sync_", "")
    for key, value in OBJECT_TYPE_MAPPING.items()
}


def get_addon_prefs():
    return bpy.context.preferences.addons[__package__].preferences


def is_excluded_object(obj, prefs):
    """Check if an object type should be excluded based on user preferences"""

    # Make key - either (obj.type, obj.empty_display_type) or (obj.type, None)
    obj_type = (obj.type, obj.empty_display_type if obj.type == 'EMPTY' else None)

    # Get prop name via obj type key
    prop_name, _ = OBJECT_TYPE_MAPPING.get(obj_type)

    # If the object type is not mapped, don't exclude
    if prop_name is None:
        return False

    # Check if the property is disabled in preferences
    is_disabled = not getattr(prefs, prop_name, False)

    return is_disabled


def sync_object_data_name(obj, prefs):
    if obj and obj.data:
        if is_excluded_object(obj, prefs):
            return

        type_prefix, type_suffix = get_per_object_affixes(obj, prefs)
        prefix = prefs.prefix
        suffix = prefs.suffix

        # Check for multiple users
        if obj.data.users > 1 and prefs.multi_user_behavior == 'NOTHING':
            return

        new_data_name = prefix + type_prefix + obj.name + type_suffix + suffix
        old_data_name = obj.data.name

        obj.data.name = new_data_name
        if obj.data.name != new_data_name:
            force_rename(obj, new_data_name, old_data_name)

        if prefs.resync:
            obj.name = new_data_name


def get_per_object_affixes(obj, prefs):
    obj_type = (obj.type, obj.empty_display_type if obj.type == 'EMPTY' else None)

    type_name = TYPE_TO_AFFIX.get(obj_type)

    prefix_attr = f"{type_name}_prefix"
    suffix_attr = f"{type_name}_suffix"

    type_prefix = getattr(prefs, prefix_attr)
    type_suffix = getattr(prefs, suffix_attr)

    return type_prefix, type_suffix


def force_rename(obj, new_data_name, old_data_name):
    """Temporarily rename the conflicting data block"""
    obj_type = (obj.type, obj.empty_display_type if obj.type == 'EMPTY' else None)

    _, data_col_str = OBJECT_TYPE_MAPPING.get(obj_type)

    data_col = getattr(bpy.data, data_col_str)

    root_name, _, _ = old_data_name.rpartition('.')

    temp_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 25)))

    data_col[new_data_name].name = temp_name
    obj.data.name = new_data_name
    data_col[temp_name].name = root_name + ".001"  # Here Blender should automatically find the lowest increment


MULTI_USER_OBJECT_DATA = set()


def run_on_sync_complete(obj, prefs):
    """Adds multi user data to MULTI_USER_OBJECT_DATA for warnings"""
    if obj and obj.data:
        if is_excluded_object(obj, prefs):
            return
        global MULTI_USER_OBJECT_DATA
        if obj.data and obj.data.users > 1:
            MULTI_USER_OBJECT_DATA.add(obj.data.name)


def notify():
    """Msgbus call back to run auto sync operator"""
    bpy.ops.object.auto_sync_object_data_name()


def register_msgbus():
    bpy.msgbus.subscribe_rna(
        key=(bpy.types.Object, "name"),
        owner=__package__,
        args=(),
        notify=notify,
    )


def unregister_msgbus():
    bpy.msgbus.clear_by_owner(__package__)


@persistent
def on_load_post(dummy):
    """Persistent handler to re-register msgbus on file load"""
    unregister_msgbus()
    register_msgbus()


class OBJECT_OT_auto_sync_object_data_name(bpy.types.Operator):
    """Automatically syncs object data name with object name"""

    bl_idname = "object.auto_sync_object_data_name"
    bl_label = "Auto Sync Data Name"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        objects = set(bpy.context.selected_objects)
        prefs = get_addon_prefs()

        for obj in objects:
            sync_object_data_name(obj, prefs)

        if prefs.multi_user_warning:
            for obj in objects:
                run_on_sync_complete(obj, prefs)

            if MULTI_USER_OBJECT_DATA:
                message = "Object data has multiple users: " + ", ".join(sorted(MULTI_USER_OBJECT_DATA))

                def draw(self, context):
                    self.layout.label(text=message)
                # It seems that self.report doesn't show up in the status bar because it
                # is called by python and not in the UI
                # Pop up is a bit annoying but better than nothing
                bpy.context.window_manager.popup_menu(draw, title="Warning", icon='INFO')
                self.report({'INFO'}, message)  # Still useful since it prints to the console
                MULTI_USER_OBJECT_DATA.clear()

        return {'FINISHED'}


class OBJECT_OT_sync_object_data_name(bpy.types.Operator):
    """Synchronize object data names"""

    bl_idname = "object.sync_object_data_name"
    bl_label = "Sync Object Data Names"
    bl_options = {'REGISTER', 'UNDO'}

    sync_scope: bpy.props.EnumProperty(
        name="Affect",
        description="Which objects to affect",
        items=[
            ('SELECTED', "Selected", "Sync selected objects"),
            ('ALL', "All", "Sync all objects in the blend file"),
        ],
        default='SELECTED',
    )

    include_children: bpy.props.BoolProperty(
        name="Include Children",
        description="Include children of selected objects",
        default=False
    )

    inverse_operation: bpy.props.BoolProperty(
        name="Inverse",
        description="Inverse the syncing operation (Object Data Name -> Object Name)",
        default=False
    )

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        row = layout.row()
        row.prop(self, "sync_scope", expand=True)

        row = layout.row()
        row.active = (self.sync_scope == 'SELECTED')
        row.prop(self, "include_children")

        row = layout.row()
        row.prop(self, "inverse_operation")

    def execute(self, context):
        objects = set()
        prefs = get_addon_prefs()

        if self.sync_scope == 'SELECTED':
            objects.update(context.selected_objects)

            if self.include_children:
                for obj in context.selected_objects:
                    objects.update(self.get_children_recursive(obj))
        else:
            objects.update(bpy.data.objects)

        if self.inverse_operation:
            unregister_msgbus()
            for obj in objects:
                self.sync_object_name(obj, prefs)
            register_msgbus()

        else:
            for obj in objects:
                sync_object_data_name(obj, prefs)

            if prefs.multi_user_warning:
                for obj in objects:
                    run_on_sync_complete(obj, prefs)

        if MULTI_USER_OBJECT_DATA:
            message = "Object data has multiple users: " + ", ".join(sorted(MULTI_USER_OBJECT_DATA))
            self.report({'INFO'}, message)
            MULTI_USER_OBJECT_DATA.clear()

        return {'FINISHED'}

    def sync_object_name(self, obj, prefs):
        if obj and obj.data:
            if is_excluded_object(obj, prefs):
                return
            obj.name = obj.data.name

    def get_children_recursive(self, obj):
        children = []
        for child in obj.children:
            children.append(child)
            children.extend(self.get_children_recursive(child))
        return children


def menu_add(self, context):
    self.layout.separator()
    self.layout.operator(OBJECT_OT_sync_object_data_name.bl_idname)


def register():
    register_msgbus()
    bpy.app.handlers.load_post.append(on_load_post)
    bpy.utils.register_class(OBJECT_OT_sync_object_data_name)
    bpy.utils.register_class(OBJECT_OT_auto_sync_object_data_name)
    bpy.types.VIEW3D_MT_object.append(menu_add)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_add)


def unregister():
    unregister_msgbus()
    bpy.app.handlers.load_post.remove(on_load_post)
    bpy.utils.unregister_class(OBJECT_OT_sync_object_data_name)
    bpy.utils.unregister_class(OBJECT_OT_auto_sync_object_data_name)
    bpy.types.VIEW3D_MT_object.remove(menu_add)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_add)

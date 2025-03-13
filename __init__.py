bl_info = {
    "name": "Auto Sync Object Data Name",
    "description": "Automatically sync object data name with object name, with optional behavior settings.",
    "author": "GeeDoubleU",
    "blender": (2, 83, 0),
    "location": "View3D -> Object",
    "category": "Object",
    "version": (1, 0, 0),
}

import bpy
from bpy.app.handlers import persistent

#Addon prefs
class ASODN_addon_preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    multi_user_behavior: bpy.props.EnumProperty(
        name="Multi User Behavior",
        description="What to do when object data has multiple users",
        items=[
            ('RENAME', "Rename", "Renames object data every time one of its users is renamed"),
            ('NOTHING', "Do Nothing", "Leaves object data name unchanged"),
        ],
        default='RENAME',

    )
    multi_user_warning: bpy.props.BoolProperty(
        name="Warn",
        description="Warn the user if object data has multiple users",
        default=False,
    )

    prefix: bpy.props.StringProperty(
        name="Prefix",
        description="Prefix to add to object data names",
        default="",
    )

    # Boolean properties for each object type
    sync_mesh: bpy.props.BoolProperty(
        name="Mesh",
        description="Sync mesh names",
        default=True,
    )
    
    sync_curve: bpy.props.BoolProperty(
        name="Curve",
        description="Sync curve names",
        default=True,
    )
    
    sync_surface: bpy.props.BoolProperty(
        name="Surface",
        description="Sync surface names",
        default=True,
    )
    
    sync_meta: bpy.props.BoolProperty(
        name="Meta",
        description="Sync meta names",
        default=True,
    )
    
    sync_text: bpy.props.BoolProperty(
        name="Text",
        description="Sync text names",
        default=True,
    )
    
    sync_hair: bpy.props.BoolProperty(
        name="Hair Curves",
        description="Sync hair curve names",
        default=True,
    )

    sync_pointcloud: bpy.props.BoolProperty(
        name="Point Cloud",
        description="Sync point cloud names",
        default=True,
    )
    
    sync_volume: bpy.props.BoolProperty(
        name="Volume",
        description="Sync volume names",
        default=True,
    )
    
    sync_gpencil: bpy.props.BoolProperty(
        name="Grease Pencil",
        description="Sync grease pencil names",
        default=True,
    )
    
    sync_armature: bpy.props.BoolProperty(
        name="Armature",
        description="Sync armature names",
        default=True,
    )
    
    sync_lattice: bpy.props.BoolProperty(
        name="Lattice",
        description="Sync lattice names",
        default=True,
    )
    
    sync_image: bpy.props.BoolProperty(
        name="Image",
        description="Sync image names",
        default=True,
    )

    sync_light: bpy.props.BoolProperty(
        name="Light",
        description="Sync light names",
        default=True,
    )
    
    sync_lightprobe: bpy.props.BoolProperty(
        name="Light Probe",
        description="Sync light probe names",
        default=True,
    )
    
    sync_camera: bpy.props.BoolProperty(
        name="Camera",
        description="Sync camera names",
        default=True,
    )
    
    sync_speaker: bpy.props.BoolProperty(
        name="Speaker",
        description="Sync speaker names",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        box = layout.box()
        box.label(text="Sync Settings", icon="SETTINGS")

        col = box.column()

        # Multi user behavior settings
        row = col.row()
        row.prop(self, "multi_user_behavior", expand=True)

        row = col.row(align=True)
        row.prop(self, "multi_user_warning")
        
        # Prefix setting
        row = box.row()
        row.prop(self, "prefix")
        
        # Object type toggles
        layout.use_property_split = False
        box = layout.box()
        box.label(text="Affected Object Types", icon="OBJECT_DATAMODE")
        col = box.column()
       
        col.prop(self, "sync_mesh", icon='OUTLINER_OB_MESH')
        col.prop(self, "sync_curve", icon='OUTLINER_OB_CURVE')
        col.prop(self, "sync_surface", icon='OUTLINER_OB_SURFACE')
        col.prop(self, "sync_meta", icon='OUTLINER_OB_META')
        col.prop(self, "sync_text", icon='OUTLINER_OB_FONT')
        col.prop(self, "sync_hair", icon='OUTLINER_OB_CURVES')
        col.prop(self, "sync_pointcloud", icon='OUTLINER_OB_POINTCLOUD')
        col.prop(self, "sync_volume", icon='OUTLINER_OB_VOLUME')
        col.prop(self, "sync_gpencil", icon='OUTLINER_OB_GREASEPENCIL')
        col.prop(self, "sync_armature", icon='OUTLINER_OB_ARMATURE')
        col.prop(self, "sync_lattice", icon='OUTLINER_OB_LATTICE')
        col.prop(self, "sync_image", icon='OUTLINER_OB_IMAGE')
        col.prop(self, "sync_light", icon='OUTLINER_OB_LIGHT')
        col.prop(self, "sync_lightprobe", icon='OUTLINER_OB_LIGHTPROBE')
        col.prop(self, "sync_camera", icon='OUTLINER_OB_CAMERA')
        col.prop(self, "sync_speaker", icon='OUTLINER_OB_SPEAKER')

# Mapping between Blender object types and preferences
OBJECT_TYPE_MAPPING = {
    ('MESH', None): "sync_mesh",
    ('CURVE', None): "sync_curve",
    ('SURFACE', None): "sync_surface",
    ('META', None): "sync_meta",
    ('FONT', None): "sync_text",
    ('CURVES', None): "sync_hair",
    ('POINTCLOUD', None): "sync_pointcloud",
    ('VOLUME', None): "sync_volume",
    ('GPENCIL', None): "sync_gpencil",
    ('ARMATURE', None): "sync_armature",
    ('LATTICE', None): "sync_lattice",
    ('EMPTY', 'IMAGE'): "sync_image",
    ('LIGHT', None): "sync_light",
    ('LIGHT_PROBE', None): "sync_lightprobe",
    ('CAMERA', None): "sync_camera",
    ('SPEAKER', None): "sync_speaker",
}

addon_prefs_cache = None

def get_addon_prefs():
    """Retrieve cached add-on preferences or refresh cache if needed."""
    global addon_prefs_cache
    if not addon_prefs_cache:
        addon_prefs_cache = bpy.context.preferences.addons[__name__].preferences
    return addon_prefs_cache

# Function to get excluded object types based on preferences
def get_excluded_object_types():
    excluded = set()
    prefs = get_addon_prefs()

    for obj_type, prop_name in OBJECT_TYPE_MAPPING.items():
        if not getattr(prefs, prop_name):
            excluded.add(obj_type)
    
    return excluded

def sync_object_data_name(obj):
    if obj and obj.data:
        # Check if object type is in excluded list
        obj_type = (obj.type, obj.empty_display_type if obj.type == 'EMPTY' else None)
        if obj_type in get_excluded_object_types():
            return
            
        prefs = get_addon_prefs()
        prefix = prefs.prefix

        # Check for multiple users
        if obj.data.users > 1 and prefs.multi_user_behavior == 'NOTHING':
            return

        new_data_name = prefix + obj.name
        if obj.data.name != new_data_name:
            obj.data.name = new_data_name

MULTI_USER_OBJECT_DATA = set()

# Adds multi user data to MULTI_USER_OBJECT_DATA
def run_on_sync_complete(obj):
    global MULTI_USER_OBJECT_DATA
    if obj.data and obj.data.users > 1:
            MULTI_USER_OBJECT_DATA.add(obj.data.name)

#Msgbus call back
def notify():
    bpy.ops.object.auto_sync_object_data_name()

# Register msgbus to listen for object rename
def register_msgbus():
    bpy.msgbus.subscribe_rna(
        key=(bpy.types.Object, "name"),
        owner=__name__,
        args=(),
        notify=notify,
    )

def unregister_msgbus():
    bpy.msgbus.clear_by_owner(__name__)

# Persistent handler to re-register msgbus on file load
@persistent
def on_load_post(dummy):
    unregister_msgbus()
    register_msgbus()

# Used internally by msgbus call back to auto sync object data name with object name
class OBJECT_OT_auto_sync_object_data_name(bpy.types.Operator):
    """Automatically syncs object data name with object name"""

    bl_idname = "object.auto_sync_object_data_name"
    bl_label = "Auto Sync Data Name"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}
    
    def execute(self, context):
        objects = set(bpy.context.selected_objects)
        active_obj = bpy.context.view_layer.objects.active
        prefs = get_addon_prefs()

        if active_obj:
            objects.add(active_obj)

        for obj in objects:
            sync_object_data_name(obj)
       
        if prefs.multi_user_behavior:
            for obj in objects:
                run_on_sync_complete(obj)

            if MULTI_USER_OBJECT_DATA:
                message = "Object data has multiple users: " + ", ".join(sorted(MULTI_USER_OBJECT_DATA))
                def draw(self, context):
                    self.layout.label(text=message)
                # It seems that self.report doesn't show up in the status bar because it is called by python and not in the UI
                bpy.context.window_manager.popup_menu(draw, title="Warning", icon='INFO') # Pop up is a bit annoying but better than nothing
                self.report({'INFO'}, message) # Still useful since it prints to the console
                MULTI_USER_OBJECT_DATA.clear()

        return {'FINISHED'}

# Operator for mass name syncing with aditonal options
class OBJECT_OT_sync_object_data_name(bpy.types.Operator):
    """Synchronize object data names"""

    bl_idname = "object.sync_object_data_name"
    bl_label = "Sync Object Data Names"
    bl_options = {'REGISTER', 'UNDO'}
    
    sync_scope: bpy.props.EnumProperty(
        name="Affect",
        description="Which objects to affect",
        items=[
            ('SELECTED', "Selected", "Only sync selected objects"),
            ('ALL', "All", "Sync all objects in the active scene"),
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
        prefs = get_addon_prefs()
        objects = set()

        if self.sync_scope == 'SELECTED':
            objects.update(context.selected_objects)

            if self.include_children:
                for obj in context.selected_objects:
                    objects.update(self.get_children_recursive(obj))
        else:
            objects.update(context.scene.objects)
        
        if self.inverse_operation:
            unregister_msgbus()
            for obj in objects:
                self.sync_object_name(obj)
            register_msgbus()

        else:
            for obj in objects:
                sync_object_data_name(obj)

            if prefs.multi_user_warning:
                for obj in objects:
                    run_on_sync_complete(obj)
        
        if MULTI_USER_OBJECT_DATA:
            message = "Object data has multiple users: " + ", ".join(sorted(MULTI_USER_OBJECT_DATA))
            self.report({'INFO'}, message)
            MULTI_USER_OBJECT_DATA.clear()

        return {'FINISHED'}
    
    def sync_object_name(self, obj):
        if obj and obj.data:
            if obj.name != obj.data.name:
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

# Addon registration
def register():
    register_msgbus()
    bpy.utils.register_class(ASODN_addon_preferences)
    bpy.app.handlers.load_post.append(on_load_post)
    bpy.utils.register_class(OBJECT_OT_sync_object_data_name)
    bpy.utils.register_class(OBJECT_OT_auto_sync_object_data_name)
    bpy.types.VIEW3D_MT_object.append(menu_add)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_add)

# Addon unregistration
def unregister():
    unregister_msgbus()
    bpy.utils.unregister_class(ASODN_addon_preferences)
    bpy.app.handlers.load_post.remove(on_load_post)
    bpy.utils.unregister_class(OBJECT_OT_sync_object_data_name)
    bpy.utils.unregister_class(OBJECT_OT_auto_sync_object_data_name)
    bpy.types.VIEW3D_MT_object.remove(menu_add)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_add)
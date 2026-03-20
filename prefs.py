import bpy


class ASODN_addon_preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

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
    suffix: bpy.props.StringProperty(
        name="Suffix",
        description="Suffix to add to object data names",
        default="",
    )
    # Per-object affixes
    mesh_prefix: bpy.props.StringProperty(
        name="Mesh Prefix",
        description="Prefix to add to mesh data names",
        default="",
    )
    mesh_suffix: bpy.props.StringProperty(
        name="Mesh Suffix",
        description="Suffix to add to mesh data names",
        default="",
    )
    curve_prefix: bpy.props.StringProperty(
        name="Curve Prefix",
        description="Prefix to add to curve data names",
        default="",
    )
    curve_suffix: bpy.props.StringProperty(
        name="Curve Suffix",
        description="Suffix to add to curve data names",
        default="",
    )
    surface_prefix: bpy.props.StringProperty(
        name="Surface Prefix",
        description="Prefix to add to surface data names",
        default="",
    )
    surface_suffix: bpy.props.StringProperty(
        name="Surface Suffix",
        description="Suffix to add to surface data names",
        default="",
    )
    meta_prefix: bpy.props.StringProperty(
        name="Meta Prefix",
        description="Prefix to add to meta data names",
        default="",
    )
    meta_suffix: bpy.props.StringProperty(
        name="Meta Suffix",
        description="Suffix to add to meta data names",
        default="",
    )
    text_prefix: bpy.props.StringProperty(
        name="Text Prefix",
        description="Prefix to add to text data names",
        default="",
    )
    text_suffix: bpy.props.StringProperty(
        name="Text Suffix",
        description="Suffix to add to text data names",
        default="",
    )
    hair_prefix: bpy.props.StringProperty(
        name="Text Prefix",
        description="Prefix to add to text data names",
        default="",
    )
    hair_suffix: bpy.props.StringProperty(
        name="Hair Suffix",
        description="Suffix to add to hair data names",
        default="",
    )
    pointcloud_prefix: bpy.props.StringProperty(
        name="Point Cloud Prefix",
        description="Prefix to add to point cloud data names",
        default="",
    )
    pointcloud_suffix: bpy.props.StringProperty(
        name="Point Cloud Suffix",
        description="Suffix to add to point cloud data names",
        default="",
    )
    volume_prefix: bpy.props.StringProperty(
        name="Volume Prefix",
        description="Prefix to add to volume data names",
        default="",
    )
    volume_suffix: bpy.props.StringProperty(
        name="Volume Suffix",
        description="Suffix to add to volume data names",
        default="",
    )
    greasepencil_prefix: bpy.props.StringProperty(
        name="Grease Pencil Prefix",
        description="Prefix to add to grease pencil data names",
        default="",
    )
    greasepencil_suffix: bpy.props.StringProperty(
        name="Grease Pencil Suffix",
        description="Suffix to add to grease pencil data names",
        default="",
    )
    armature_prefix: bpy.props.StringProperty(
        name="Armature Prefix",
        description="Prefix to add to armature data names",
        default="",
    )
    armature_suffix: bpy.props.StringProperty(
        name="Armature Suffix",
        description="Suffix to add to armature data names",
        default="",
    )
    lattice_prefix: bpy.props.StringProperty(
        name="Lattice Prefix",
        description="Prefix to add to lattice data names",
        default="",
    )
    lattice_suffix: bpy.props.StringProperty(
        name="Lattice Suffix",
        description="Suffix to add to lattice data names",
        default="",
    )
    image_prefix: bpy.props.StringProperty(
        name="Image Prefix",
        description="Prefix to add to image data names",
        default="",
    )
    image_suffix: bpy.props.StringProperty(
        name="Image Suffix",
        description="Suffix to add to image data names",
        default="",
    )
    light_prefix: bpy.props.StringProperty(
        name="Light Prefix",
        description="Prefix to add to light data names",
        default="",
    )
    light_suffix: bpy.props.StringProperty(
        name="Light Suffix",
        description="Suffix to add to light data names",
        default="",
    )
    lightprobe_prefix: bpy.props.StringProperty(
        name="Light Probe Prefix",
        description="Prefix to add to light probe data names",
        default="",
    )
    lightprobe_suffix: bpy.props.StringProperty(
        name="Light Probe Suffix",
        description="Suffix to add to light probe data names",
        default="",
    )
    camera_prefix: bpy.props.StringProperty(
        name="Camera Prefix",
        description="Prefix to add to camera data names",
        default="",
    )
    camera_suffix: bpy.props.StringProperty(
        name="Camera Suffix",
        description="Suffix to add to camera data names",
        default="",
    )
    speaker_prefix: bpy.props.StringProperty(
        name="Speaker Prefix",
        description="Prefix to add to speaker data names",
        default="",
    )
    speaker_suffix: bpy.props.StringProperty(
        name="Speaker Suffix",
        description="Suffix to add to speaker data names",
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
    sync_greasepencil: bpy.props.BoolProperty(
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
    show_sync_settings: bpy.props.BoolProperty(
        name="Show sync settings",
        default=False,
        description="Show settings for name syncing",
    )
    show_affixes_settings: bpy.props.BoolProperty(
        name="Show affixes settings",
        default=False,
        description="Show settings for affixes",
    )
    show_object_types: bpy.props.BoolProperty(
        name="Show object types",
        default=False,
        description="Show toggles for object types",
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        icon_curves = 'OUTLINER_OB_CURVES' if bpy.app.version >= (3, 2, 0) else 'OUTLINER_OB_HAIR'

        # Sync settings
        sync_box = layout.box()
        sync_col = sync_box.column()

        if draw_dropdown(sync_col, self, 'show_sync_settings', "Sync Settings", 'SETTINGS'):

            # Multi user behavior settings
            row = sync_col.row()
            row.prop(self, "multi_user_behavior", expand=True)

            row = sync_col.row(align=True)
            row.prop(self, "multi_user_warning")
            
            # Affixes settings
            affixes_box = sync_box.box()
            affixes_col = affixes_box.column()

            if draw_dropdown(affixes_col, self, 'show_affixes_settings', "Affixes", 'SORTBYEXT'):
                affixes_col.use_property_split = False
                draw_affixes_row(affixes_col, self, "Global", 'OBJECT_DATA', "prefix", "suffix")
                draw_affixes_row(affixes_col, self, "Mesh", 'OUTLINER_OB_MESH', "mesh_prefix", "mesh_suffix")
                draw_affixes_row(affixes_col, self, "Curve", 'OUTLINER_OB_CURVE', "curve_prefix", "curve_suffix")
                draw_affixes_row(affixes_col, self, "Surface", 'OUTLINER_OB_SURFACE', "surface_prefix", "surface_suffix")
                draw_affixes_row(affixes_col, self, "Meta", 'OUTLINER_OB_META', "meta_prefix", "meta_suffix")
                draw_affixes_row(affixes_col, self, "Text", 'OUTLINER_OB_FONT', "text_prefix", "text_suffix")
                draw_affixes_row(affixes_col, self, "Hair", icon_curves, "hair_prefix", "hair_suffix")
                draw_affixes_row(affixes_col, self, "Point Cloud", 'OUTLINER_OB_POINTCLOUD', "pointcloud_prefix", "pointcloud_suffix")
                draw_affixes_row(affixes_col, self, "Volume", 'OUTLINER_OB_VOLUME', "volume_prefix", "volume_suffix")
                draw_affixes_row(affixes_col, self, "Grease Pencil", 'OUTLINER_OB_GREASEPENCIL', "greasepencil_prefix", "greasepencil_suffix")
                draw_affixes_row(affixes_col, self, "Armature", 'OUTLINER_OB_ARMATURE', "armature_prefix", "armature_suffix")
                draw_affixes_row(affixes_col, self, "Lattice", 'OUTLINER_OB_LATTICE', "lattice_prefix", "lattice_suffix")
                draw_affixes_row(affixes_col, self, "Image", 'OUTLINER_OB_IMAGE', "image_prefix", "image_suffix")
                draw_affixes_row(affixes_col, self, "Light", 'OUTLINER_OB_LIGHT', "light_prefix", "light_suffix")
                draw_affixes_row(affixes_col, self, "Light Probe", 'OUTLINER_OB_LIGHTPROBE', "lightprobe_prefix", "lightprobe_suffix")
                draw_affixes_row(affixes_col, self, "Camera", 'OUTLINER_OB_CAMERA', "camera_prefix", "camera_suffix")
                draw_affixes_row(affixes_col, self, "Speaker", 'OUTLINER_OB_SPEAKER', "speaker_prefix", "speaker_suffix")

        # Object type toggles
        obj_type_box = layout.box()
        obj_type_col = obj_type_box.column()
        
        if draw_dropdown(obj_type_col, self, 'show_object_types', "Affected Object Types", 'OBJECT_DATAMODE'):
            obj_type_col.use_property_split = False
            obj_type_col.prop(self, "sync_mesh", icon='OUTLINER_OB_MESH')
            obj_type_col.prop(self, "sync_curve", icon='OUTLINER_OB_CURVE')
            obj_type_col.prop(self, "sync_surface", icon='OUTLINER_OB_SURFACE')
            obj_type_col.prop(self, "sync_meta", icon='OUTLINER_OB_META')
            obj_type_col.prop(self, "sync_text", icon='OUTLINER_OB_FONT')
            obj_type_col.prop(self, "sync_hair", icon=icon_curves)
            obj_type_col.prop(self, "sync_pointcloud", icon='OUTLINER_OB_POINTCLOUD')
            obj_type_col.prop(self, "sync_volume", icon='OUTLINER_OB_VOLUME')
            obj_type_col.prop(self, "sync_greasepencil", icon='OUTLINER_OB_GREASEPENCIL')
            obj_type_col.prop(self, "sync_armature", icon='OUTLINER_OB_ARMATURE')
            obj_type_col.prop(self, "sync_lattice", icon='OUTLINER_OB_LATTICE')
            obj_type_col.prop(self, "sync_image", icon='OUTLINER_OB_IMAGE')
            obj_type_col.prop(self, "sync_light", icon='OUTLINER_OB_LIGHT')
            obj_type_col.prop(self, "sync_lightprobe", icon='OUTLINER_OB_LIGHTPROBE')
            obj_type_col.prop(self, "sync_camera", icon='OUTLINER_OB_CAMERA')
            obj_type_col.prop(self, "sync_speaker", icon='OUTLINER_OB_SPEAKER')


def draw_dropdown(layout, data, expand_prop, label, icon):
    row = layout.row(align=True)
    row.use_property_split = False
    sub = row.row(align=True)  # Sub stops label from getting clipped by ghost button
    sub.alignment = 'LEFT'

    expanded = getattr(data, expand_prop)
    arrow = 'DOWNARROW_HLT' if expanded else 'RIGHTARROW'

    sub.prop(data, expand_prop, icon=arrow, emboss=False, text="")
    sub.prop(data, expand_prop, icon=icon, emboss=False, text=label)
    # Below creates a ghost button that streches horizontally so we don't have to click dirrectly on the label
    sub = row.row(align=True)
    sub.alignment = 'LEFT'
    sub.scale_x = 100
    sub.prop(data, expand_prop, icon='BLANK1', emboss=False, text="")

    return expanded

def draw_affixes_row(layout, data, label, icon, prefix_prop, suffix_prop):
    split = layout.split(align=True)

    split.label(text=label, icon=icon)
    split.prop(data, prefix_prop, text="", placeholder="Prefix")
    split.prop(data, suffix_prop, text="", placeholder="Suffix")


def register():
    bpy.utils.register_class(ASODN_addon_preferences)


def unregister():
    bpy.utils.unregister_class(ASODN_addon_preferences)

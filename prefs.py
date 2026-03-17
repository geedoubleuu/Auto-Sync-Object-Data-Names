import bpy

#Addon prefs
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
    show_object_types: bpy.props.BoolProperty(
        name="Show object types",
        default=False,
        description="Show toggles for object types",
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        # Sync settings
        box = layout.box()
        col = box.column()

        if draw_dropdown(col, self, 'show_sync_settings', "Sync Settings", 'SETTINGS'):

            # Multi user behavior settings
            row = col.row()
            row.prop(self, "multi_user_behavior", expand=True)

            row = col.row(align=True)
            row.prop(self, "multi_user_warning")
            
            # Prefix setting
            row = box.row()
            row.prop(self, "prefix")
            
        # Object type toggles
        icon_curves = 'OUTLINER_OB_CURVES' if bpy.app.version >= (3, 2, 0) else 'OUTLINER_OB_HAIR'
        box = layout.box()
        col = box.column()
        
        if draw_dropdown(col, self, 'show_object_types', "Affected Object Types", 'OBJECT_DATAMODE'):

            col.use_property_split = False
            
            col.prop(self, "sync_mesh", icon='OUTLINER_OB_MESH')
            col.prop(self, "sync_curve", icon='OUTLINER_OB_CURVE')
            col.prop(self, "sync_surface", icon='OUTLINER_OB_SURFACE')
            col.prop(self, "sync_meta", icon='OUTLINER_OB_META')
            col.prop(self, "sync_text", icon='OUTLINER_OB_FONT')
            col.prop(self, "sync_hair", icon=icon_curves)
            col.prop(self, "sync_pointcloud", icon='OUTLINER_OB_POINTCLOUD')
            col.prop(self, "sync_volume", icon='OUTLINER_OB_VOLUME')
            col.prop(self, "sync_greasepencil", icon='OUTLINER_OB_GREASEPENCIL')
            col.prop(self, "sync_armature", icon='OUTLINER_OB_ARMATURE')
            col.prop(self, "sync_lattice", icon='OUTLINER_OB_LATTICE')
            col.prop(self, "sync_image", icon='OUTLINER_OB_IMAGE')
            col.prop(self, "sync_light", icon='OUTLINER_OB_LIGHT')
            col.prop(self, "sync_lightprobe", icon='OUTLINER_OB_LIGHTPROBE')
            col.prop(self, "sync_camera", icon='OUTLINER_OB_CAMERA')
            col.prop(self, "sync_speaker", icon='OUTLINER_OB_SPEAKER')

def draw_dropdown(layout, data, expand_prop, label, icon):
    row = layout.row(align=True)
    row.use_property_split = False
    sub = row.row(align=True) # Sub stops label from getting clipped by ghost button
    sub.alignment='LEFT'

    expanded = getattr(data, expand_prop)
    arrow = 'DOWNARROW_HLT' if expanded else 'RIGHTARROW'

    sub.prop(data, expand_prop, icon=arrow, emboss=False, text="")
    sub.prop(data, expand_prop, icon=icon, emboss=False, text=label)
    # Below creates a ghost button that streches horizontally so we don't have to click dirrectly on the label
    sub = row.row(align=True)
    sub.alignment='LEFT'
    sub.scale_x = 100
    sub.prop(data, expand_prop, icon='BLANK1', emboss=False, text="")

    return expanded

# Addon registration
def register():
    bpy.utils.register_class(ASODN_addon_preferences)

# Addon unregistration
def unregister():
    bpy.utils.unregister_class(ASODN_addon_preferences)

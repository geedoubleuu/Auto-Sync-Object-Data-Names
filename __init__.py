bl_info = {
    "name": "Auto Sync Object Data Names",
    "description": "Automatically sync object data name with object name, with optional behavior settings.",
    "author": "GeeDoubleU",
    "blender": (4, 0, 0),
    "location": "View3D > Object",
    "category": "Object",
    "version": (1, 0, 0),
}

import bpy
from . import prefs, core


def register():
    prefs.register()
    core.register()


def unregister():
    prefs.unregister()
    core.unregister()

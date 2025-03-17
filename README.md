# Auto-Sync-Object-Data-Name
**Auto Sync Object Data Name** is a Blender add-on that automatically synchronizes object data names with their corresponding object names. This helps maintain a clean and organized naming convention, especially when working with multiple objects and shared object data.

## Features
- Automatically renames object data to match object names.

- Allows setting a custom prefix for object data names.

- Handles multi-user object data, with options to rename or leave unchanged.

- Ability to disable specific object types (Meshes, Curves, Lights, Cameras, etc.).

- Provides an option to warn the user if object data has multiple users.

## Compatibility

## Installation

## Addon Preferences
After installing the add-on, you can find its preferences under:
`Edit > Preferences > Add-ons > Auto Sync Object Data Name`.

### 1. Multi User Behavior

Determines what happens when an object's data block has multiple users:

- **Rename:** Renames object data every time one of its users is renamed.

- **Do Nothing:** Leaves object data names unchanged.

### 2. Multi User Warning

- **Enabled:** Displays a warning if object data is shared among multiple objects.

- **Disabled:** No warning is shown.

### 3. Prefix

- Adds a custom prefix to new object data names.

### 4. Affected Object Types

- Choose which object types should be affected.

## Operator
This addon also comes with an operator to manually sync names for multiple objects

**Mode:** `Object Mode`

**Menu:** `Object > Sync Object Data Names` OR `RMB > Sync Object Data Names`

### Affect

- **Selected:** Syncs the names of selected objects only.

- **All:** Syncs the names of all objects in the active scene.

### Options

- **Include Children:** Includes the children of selected objects recursively.

- **Inverse:** The object's name is replaced with the object data name.
  
> [!NOTE]
> **Inverse** does not use the addon's preferences.

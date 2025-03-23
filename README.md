# Auto-Sync-Object-Data-Names
**Auto Sync Object Data Names** is a Blender add-on that automatically synchronizes object data names with their corresponding object names.

![auto_sync_object_data_name_banner](https://github.com/user-attachments/assets/9298c3d8-d734-4659-9bf4-f1471fd2e163)


## Features
- Automatically renames object data to match object names.

- Allows setting a custom prefix for object data names.

- Handles multi-user object data, with options to rename or leave unchanged.

- Ability to disable specific object types (Meshes, Curves, Lights, Cameras, etc.).

- Provides an option to warn the user if object data has multiple users.

## Compatibility
- Blender `4.0.0` or later is recommended.

- May work for earlier Blender versions but no support will be provided if not fully working.

## Installation
1. Download the `.zip` file from the GitHub repository.

2. Open Blender and navigate to `Edit > Preferences > Add-ons`.

3. Click `Install from Disk...` in the dropdown menu at the top right.

4. Select the downloaded `.zip` file and install it.

## Add-on Preferences
After installing the add-on, you can find its preferences under:
`Edit > Preferences > Add-ons > Auto Sync Object Data Name`. Preferences are hidden by default, click to expand the dropdown menu.

![sync_settings](https://github.com/user-attachments/assets/25352b11-3883-436b-859f-4a2484b37b3d)

### Multi-User Behavior

Determines what happens when an object's data block has multiple users:

- **Rename:** Renames object data every time one of its users is renamed.

- **Do Nothing:** Leaves object data names unchanged.

### Warn

- **Enabled:** Displays a warning if object data is shared among multiple objects.

- **Disabled:** No warning is shown.

### Prefix

- Adds a custom prefix to new object data names.

### Affected Object Types

- Choose which object types should be affected.

![affected_object_types](https://github.com/user-attachments/assets/cc14fe2f-ed0c-4930-b3a2-7e7261e4d11a)

## Operator
This add-on also comes with an operator to manually sync names for multiple objects.

<p align="center">
  <img width="500" alt="operator" src="https://github.com/user-attachments/assets/c0bb0f43-5dcc-4677-9703-da2ca2b13c9f">
</p>

**Mode:** `Object Mode`

**Menu:** `Object > Sync Object Data Names` OR `RMB > Sync Object Data Names`

### Affect

- **Selected:** Syncs the names of selected objects only.

- **All:** Syncs the names of all objects in the active scene.

### Options

- **Include Children:** Includes the children of selected objects recursively.

- **Inverse:** The object's name is replaced with the object data name.
  
> [!NOTE]
> **Inverse** does not use the add-on's preferences.

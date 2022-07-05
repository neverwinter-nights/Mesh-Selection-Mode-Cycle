# Mesh Selection Mode Cycle
An add-on for Blender 3D editor, version 3.x.

## Description
This add-on enables fast switching between mesh selection modes.  
The add-on provides two actions to which buttons can be assigned:
* **object.mca_mesh_selection_mode_previous** – switch to a previous mesh selection mode; 
* **object.mca_mesh_selection_mode_next** – switch to a next mesh selection mode.

Mode switch happens only if a single selection mode is enabled. E.g., if you 
enable two selection modes at the same time, the add-on will not do any changes 
to the enabled selection modes.

## Why ?
The original, built into Blender, method of switching between different 
selection modes in the mesh editing process is quite difficult. It requires a 
user to look at the keyboard, remember which button is which mode and then 
press a button `1`, `2` or `3` depending on a mode selected. Some other 3D 
editors, like the Lightwave 3D editor, provide another, a much more convenient, 
way of changing the selection mode. Which method ? Cycling through available 
modes with a key which is very easy to use. This add-on tries to implement the 
same functionality as in the Lightwave 3D editor in the Blender editor. With 
this add-on you can, for example, switch between selection modes with just a 
single key of a keyboard or a mouse.  

## Installation
1. Start the Blender. Make sure that Blender's version is **3.1** or later.
2. Open menu: **Edit** -> **Preferences** -> **Add-ons** -> `Install...`
3. Select the python file (*.py) with this add-on and press the `Install Add-on` button.  
The add-on will be added into a **Mesh** category.
4. Find the add-on in the list and enable it with a checkbox.
5. In the same **Preferences** window select the **Keymap** on the left side.
6. Navigate to the **3D View** -> **Mesh** -> **Mesh (Global)** section.
7. Press `Add New` in this section. A **none** item will appear.
8. Modify the empty item changing its **none** action to one of the following: 
* **object.mca_mesh_selection_mode_previous** – if you want to switch to a previous mesh selection mode; 
* **object.mca_mesh_selection_mode_next** – if you want to switch to a next mesh selection mode.
10. Assign a button to the action. It may be a keyboard key, a mouse button or anything you like.
11. Enjoy the Blender editor which is now more comfortable to use.

Below is an example of assignment of `Alt` + `Mouse Scroll Wheel` to both actions.   
Screenshot's width is about 1000 px. To see it, you might need to open the page in a full screen.  
![Keymap](https://raw.githubusercontent.com/neverwinter-nights/Mesh-Selection-Mode-Cycle/main/Mesh%20Selection%20Mode%20Cycle/Screenshot/key_binding_example.png)
<!-- Local link: ![Keymap](./Screenshot/key_binding_example.png) -->

## Usage
Enter the mesh editing mode. Press your key combination.  
If you had a single selection mode enabled, it will be switched to a next or a 
previous mesh selection mode depending on your settings. 

## Notes
Unfortunately, modern versions of Blender editor have bugs with controls. For 
some reason the developers of Blender decided to assign hundreds of actions to 
the **Press** event instead of the **Click** event. If your newly assigned key 
does not work, do check if there are any **Press** events assigned to the same 
key. For some reason **Press** events hijack other events and break the program. 
Me myself had to spend hours searching for the problem cause, and I had to 
re-assign hundreds of bindings to make my new bindings work. Be aware!

# mca_mesh_selection_mode_cycle.py.

# Mesh Selection Mode Cycle.

# Version 1.1.

bl_info = {
    "name": "Mesh Selection Mode Cycle",
    "description": "Cycle through mesh selection modes. Works when a single mode is selected.",
    "category": "Mesh",
    "blender": (3, 1, 0),
    "author": "McArcher",
}

import bpy


class MSM:
    # Number of possible mesh selection modes. In Blender 3.1 there are three
    # modes: Vertex, Edge, Face.
    Count = 3

    DirectionPrevious = 'prev'
    DirectionNext = 'next'

    ResultCancel = 'CANCELLED'
    ResultSuccess = 'FINISHED'

    MeshEditMode = 'EDIT_MESH'

    # Arguments for the 'bpy.ops.mesh.select_mode' method.
    SelectModeTypes = {
        1: 'VERT',
        2: 'EDGE',
        3: 'FACE'
    }


class McaMeshSelectionModePrevious(bpy.types.Operator):
    """Mesh Selection Mode Cycle: Previous"""
    bl_idname = "object.mca_mesh_selection_mode_previous"
    bl_label = "Mesh Selection Mode Cycle: Previous"

    @classmethod
    def poll(cls, context):
        return is_mesh_edit_mode_selected()

    def execute(self, context):
        return execute_generic(MSM.DirectionPrevious)


class McaMeshSelectionModeNext(bpy.types.Operator):
    """Mesh Selection Mode Cycle: Next"""
    bl_idname = "object.mca_mesh_selection_mode_next"
    bl_label = "Mesh Selection Mode Cycle: Next"

    @classmethod
    def poll(cls, context):
        return is_mesh_edit_mode_selected()

    def execute(self, context):
        return execute_generic(MSM.DirectionNext)


def register():
    bpy.utils.register_class(McaMeshSelectionModePrevious)
    bpy.utils.register_class(McaMeshSelectionModeNext)


def unregister():
    bpy.utils.unregister_class(McaMeshSelectionModeNext)
    bpy.utils.unregister_class(McaMeshSelectionModePrevious)


# Counts the enabled mesh selection modes. Returns -1 on error. Argument (msm)
# is an array. Documentation:
# https://docs.blender.org/api/current/bpy.types.ToolSettings.html#bpy.types.ToolSettings.mesh_select_mode
def count_enebled_msm(msm):
    # Is everything fine ?
    if len(msm) != MSM.Count:
        return -1

    enabled_msm_count = 0
    for idx in range(MSM.Count):
        if msm[idx] == True:
            enabled_msm_count += 1

    return enabled_msm_count


# Gets the first enabled mode (index).
# Returns -1 on error.
def get_first_selected_msm(msm):
    for idx in range(MSM.Count):
        if msm[idx] == True:
            return idx

    return -1


# Returns the previous mesh selection mode (array index).
def get_previous_msm(cur_mode):
    if cur_mode <= 0:
        return MSM.Count - 1

    return cur_mode - 1


# Returns the next mesh selection mode (array index).
def get_next_msm(cur_mode):
    if cur_mode >= MSM.Count - 1:
        return 0

    return cur_mode + 1


# Selects (applies) the mesh selection mode. This method uses a low level API,
# which is not synchronized with the selection.
def select_msm_ll(msm_idx):
    msm = []
    for i in range(MSM.Count):
        msm.append(False)

    msm[msm_idx] = True

    bpy.context.tool_settings.mesh_select_mode = msm


# Selects (applies) the mesh selection mode. This method uses a high level API,
# which is synchronized with the selection.
def select_msm(msm_idx):
    typeText = MSM.SelectModeTypes[msm_idx + 1]
    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type=typeText)


# Checks whether the mesh edit mode is selected.
def is_mesh_edit_mode_selected():
    return bpy.context.mode == MSM.MeshEditMode


# A generic method to execute various actions. Cycles through mesh selection
# modes. Changes the selected mode to a next or a previous mode if a single
# mode is selected. Does nothing if more than one mode is selected. Selects the
# first mode if no mode is selected.
def execute_generic(direction):
    if (direction != MSM.DirectionPrevious) and \
            (direction != MSM.DirectionNext):
        return {MSM.ResultCancel}

    msm = bpy.context.tool_settings.mesh_select_mode
    selections_count = count_enebled_msm(msm)

    # Exit on error.
    if selections_count < 0:
        return {MSM.ResultCancel}

    # Exit if more than one mode is selected.
    if selections_count > 1:
        return {MSM.ResultCancel}

    # Select the first mode if no mode is selected.
    if selections_count == 0:
        select_msm(0)
        return {MSM.ResultSuccess}

    # Select the next or previous mode if a single mode is selected.
    selected_idx = get_first_selected_msm(msm)

    new_idx = -1
    if direction == MSM.DirectionPrevious:
        new_idx = get_previous_msm(selected_idx)
    if direction == MSM.DirectionNext:
        new_idx = get_next_msm(selected_idx)

    select_msm(new_idx)
    return {MSM.ResultSuccess}

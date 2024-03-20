import bpy
from typing import Literal

SelectMode = Literal["VERTS", "EDGES", "FACES"]
# NOTE do not use get_args() here, the order may be different from original
# https://docs.python.org/3/library/typing.html#typing.get_args
select_modes: list[SelectMode] = ["VERTS", "EDGES", "FACES"]


def select_mode_str(context: bpy.types.Context) -> SelectMode:
    v_e_f = context.scene.tool_settings.mesh_select_mode

    for bool_, mode in zip(v_e_f, select_modes):
        if bool_:
            return mode

    raise Exception("Cannot detect selection mode")


def select_mode_str2bools(bools: list[bool]) -> SelectMode:
    for bool_, mode in zip(bools, select_modes):
        if bool_:
            return mode

    raise Exception("Cannot detect selection mode")

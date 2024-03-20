import bpy
from typing import Literal

SelectMode = Literal["VERTS", "EDGES", "FACES"]
# NOTE do not use get_args() here, the order may be different from original
# https://docs.python.org/3/library/typing.html#typing.get_args
select_modes: list[SelectMode] = ["VERTS", "EDGES", "FACES"]


def curr_select_mode(context: bpy.types.Context) -> SelectMode:
    bools = context.scene.tool_settings.mesh_select_mode

    for b, m in zip(bools, select_modes):
        if b:
            return m

    raise Exception("Cannot detect selection mode")

import bpy
import bmesh
import addon_utils
from typing import Literal

SelectMode = Literal["VERTS", "EDGES", "FACES"]
# NOTE do not use get_args() here, the order may be different from original
# https://docs.python.org/3/library/typing.html#typing.get_args
select_modes: list[SelectMode] = ["VERTS", "EDGES", "FACES"]


def assert_half_wiped_out(mode: SelectMode) -> None:
    # prepare
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.context.scene.tool_settings.mesh_select_mode = [m == mode for m in select_modes]
    bpy.ops.mesh.select_all(action="SELECT")

    # exec operator
    bpy.ops.thanos.wipe_out()
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)

    match mode:
        case "VERTS":
            expected = 4
            actual = len(bm.verts)
        case "EDGES":
            expected = 6
            actual = len(bm.edges)
        case "FACES":
            expected = 3
            actual = len(bm.faces)

    # cleanup
    bm.free()
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.delete()

    # assertion
    if actual != expected:
        raise Exception(f"{mode}: expected {expected}, actual {actual}")


def main():
    addon_utils.enable("myaddon")

    for m in select_modes:
        assert_half_wiped_out(m)


if __name__ == "__main__":
    main()

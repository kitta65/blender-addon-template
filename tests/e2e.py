import bpy
import bmesh
import addon_utils
from typing import Literal

Mode = Literal["VERTS", "EDGES", "FACES"]


def assert_half_wiped_out(mode: Mode):
    # prepare
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.scene.tool_settings.mesh_select_mode = [
        mode == "VERTS",
        mode == "EDGES",
        mode == "FACES",
    ]
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")

    # exec operator
    bpy.ops.sample.thanos_wipe_out()
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

    modes: list[Mode] = ["VERTS", "EDGES", "FACES"]
    for m in modes:
        assert_half_wiped_out(m)


if __name__ == "__main__":
    main()

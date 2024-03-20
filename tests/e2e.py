import bpy
import bmesh
import addon_utils


def main():
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.scene.tool_settings.mesh_select_mode = [True, False, False]  # vetex
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.sample.thanos_wipe_out()

    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    n_vertices = len(bm.verts)
    bm.free()
    bpy.ops.object.mode_set(mode="OBJECT")

    if n_vertices != 4:
        raise Exception(f"expected: 4, actual: {n_vertices}")


if __name__ == "__main__":
    addon_utils.enable("myaddon")
    main()

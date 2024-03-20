import bpy
import bmesh
import random

bl_info = {
    "name": "Thanos",
    "author": "kitta65",
    "version": (0, 0, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Mesh > Thanos",
    "description": "Wipe out half of the vertices / edges / faces",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample",
}


class SAMPLE_OT_Thanos(bpy.types.Operator):
    bl_idname = "sample.thanos_wipe_out"
    bl_label = "Thanos"
    bl_description = "Wipe out half of the vertices"

    bl_options = {"UNDO"}

    def execute(self, context):
        v, e, f = context.scene.tool_settings.mesh_select_mode
        me = context.object.data
        bm = bmesh.from_edit_mesh(me)

        if v:
            context = "VERTS"
            geom = bm.verts
        elif e:
            context = "EDGES"
            geom = bm.edges
        elif f:
            context = "FACES_ONLY"
            geom = bm.faces
        else:
            self.report({"ERROR"}, "cannot detect mesh_selection_mode")
            return {"CANCELLED"}

        geom = random.sample(list(geom), len(geom) // 2)
        bmesh.ops.delete(bm, geom=geom, context=context)
        bmesh.update_edit_mesh(me)
        bm.free()

        return {"FINISHED"}


def menu(cls, _):
    cls.layout.separator()
    cls.layout.operator(SAMPLE_OT_Thanos.bl_idname, icon="COMMUNITY")


classes = [SAMPLE_OT_Thanos]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_edit_mesh.append(menu)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu)

    for c in reversed(classes):
        bpy.utils.unregister_class(c)

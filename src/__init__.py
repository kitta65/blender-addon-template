import bpy

bl_info = {
    "name": "Blender Add-on Template",
    "author": "kitta65",
    "version": (0, 0, 1),
    "blender": (4, 0, 0),
    "location": "",
    "description": "",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample",
}


class SAMPLE_OT_SampleOperator(bpy.types.Operator):
    bl_idname = "sample.sample_operator"
    bl_label = "sample operator"
    bl_description = "sample operator"

    def execute(self, context):

        txt: bpy.types.Text
        for txt in bpy.data.texts:
            if not txt.name.endswith(".py"):
                continue
            txt.from_string("import bpy")  # TODO exec black

        area: bpy.types.Area
        for area in bpy.context.window.screen.areas:
            if area.type != "TEXT_EDITOR":
                continue
            bpy.ops.text.cursor_set()  # needed to refresh

        return {"FINISHED"}


classes = [SAMPLE_OT_SampleOperator]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    print("activated!")


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    print("deactivated!")

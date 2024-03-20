from contextlib import contextmanager
import bpy
import addon_utils


@contextmanager
def temp_text(string: str):
    text = bpy.data.texts.new("temp.py")
    text.from_string(string)
    try:
        yield text
    finally:
        bpy.data.texts.remove(text)


if __name__ == "__main__":
    addon_utils.enable("myaddon")

    input_str = "import  bpy\n"
    expected_str = "import bpy\n"
    actual_str: str

    with temp_text(input_str) as text:
        bpy.ops.sample.sample_operator()
        actual_str = text.as_string()

    if actual_str != expected_str:
        raise Exception("not formatted!")

#!/bin/sh
ln -s /blender/4.0/python/bin/python3.10 /usr/local/bin/python
python -m ensurepip
python -m pip install fake-bpy-module-4.0
ln -s /config/workspaces/src /blender/4.0/scripts/addons/myaddon

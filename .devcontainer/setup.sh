#!/bin/sh
cd $(dirname $0)/.. # project root

sudo ln -s /blender/4.0/python/bin/python3.10 /usr/local/bin/python
python -m ensurepip
python -m pip install fake-bpy-module-4.0
sudo ln -s $(pwd)/src /blender/4.0/scripts/addons/myaddon

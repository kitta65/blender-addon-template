FROM lscr.io/linuxserver/blender:4.0.2-ls99

RUN apt-get update && \
    apt-get -y install git && \
    rm -rf /var/lib/apt/lists/*

RUN /blender/4.0/python/bin/python3.10 -m ensurepip && \
    /blender/4.0/python/bin/python3.10 -m pip install fake-bpy-module-4.0
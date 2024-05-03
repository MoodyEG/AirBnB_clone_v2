#!/usr/bin/python3
from fabric.api import local
from time import strftime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None

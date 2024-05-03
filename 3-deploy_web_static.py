#!/usr/bin/python3
""" Main
Usage:
fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
from fabric.api import local, env, put, run  # type: ignore
import os.path
from time import strftime


env.hosts = ['52.23.178.135', '100.25.47.15']


def deploy():
    """ does both functions below """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    timenow = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        print("web_static packed: {} -> {} Bytes"
              .format(filename, os.stat(filename).st_size))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo chown -R ubuntu:ubuntu /data/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        print("New version deployed!")
        return True
    except Exception:
        return False

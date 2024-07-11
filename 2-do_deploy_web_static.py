#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["web_01", "web_02"]


def do_deploy(archive_path):
    """Distribute the archive between the web server
    Args:
        archive_path: the path of the archive
    Return:
        if the file exist - True.
        otherwise - False.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web-static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("mkdir -p /data/web-static/releases/{}/".
             format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web-static/releases/{}/".
             format(file, name)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

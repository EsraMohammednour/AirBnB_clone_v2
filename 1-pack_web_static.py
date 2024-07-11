#!/usr/bin/python3
"""Fabric script that generates a .tgz"""
from fabric.api import local
import datatime
import os.path


def do_pack():
    """Archive from the contents of the web_static"""
    d = datatime.datatime.now()
    esra = "versions/web_static_{}{}{}{}{}{}.tgz".format(d.year,
                                                         d.month,
                                                         d.day,
                                                         d.hour,
                                                         d.minute,
                                                         d.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(f"tar -cvzf {} web_static".format(esra)).failed is True:
        return None
    return esra

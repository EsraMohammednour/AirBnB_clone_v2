#!/usr/bin/python3
"""Fabric script that generates a .tgz"""
import fabric.api
import datatime
import os.path


def do_pack():
    """Archive from the contents of the web_static"""
    d = datatime.datatime.now()
    esra = f"versions/web_static_{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}.tgz"
    if os.path.isdir("versions") is False:
        if fabric.api.local("mkdir -p versions").failed is True:
            return None
    if fabric.api.local(f"tar -cvzf {esra} web_static").failed is True:
        return None
    return esra

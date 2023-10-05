#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
"""Packing"""

env.user = "ubuntu"
env.hosts = ["52.87.230.156"]


def do_pack():
    """Make .tgz file"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None

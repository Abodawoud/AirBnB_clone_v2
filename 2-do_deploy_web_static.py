#!/usr/bin/python3
from fabric.api import *
import os
"""Deploying"""


env.hosts = ['52.87.230.156', '100.26.151.67']

env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web_static"""
    if not os.path.exists(archive_path):
        return False

    try:
        li = archive_path.split('/')
        file_name = li[-1]
        releases_path = "/data/web_static/releases/{}/".format(file_name[:-4])
        tmp_path = "/tmp/{}".format(file_name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False

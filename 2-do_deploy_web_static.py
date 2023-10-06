#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import local, env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['52.87.230.156', '100.26.151.67']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        release_folder = "/data/web_static/releases/{}".format(timestamp)
        run("mkdir -p {}".format(release_folder))

        archive_filename = archive_path.split("/")[-1]
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))

        run("rm /tmp/{}".format(archive_filename))

        run("mv {}/web_static/* {}".format(release_folder, release_folder))

        run("rm -rf {}/web_static".format(release_folder))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False

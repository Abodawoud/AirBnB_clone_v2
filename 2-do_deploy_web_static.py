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
        put(archive_path, '/tmp/')

        file_name = os.path.basename(archive_path)
        release_folder = f"/data/web_static/releases/{file_name[:-4]}"

        run(f'mkdir -p {release_folder}/')

        run(f'tar -xzf /tmp/{file_name} -C {release_folder}/')

        run(f'rm /tmp/{file_name}')

        run(f'mv {release_folder}/web_static/* {release_folder}/')

        run(f'rm -rf {release_folder}/web_static/')

        run('rm -rf /data/web_static/current/')

        run(f'ln -s {release_folder}/ /data/web_static/current/')

        print('New version deployed!')
        return True
    except Exception as e:
        return False

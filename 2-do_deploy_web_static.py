#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

# Configure Fabric environment
env.user = 'ubuntu'
env.hosts = ['100.26.151.67', '52.87.230.156']
env.key_filename = os.path.expanduser('~/.ssh/id_rsa')

def do_deploy(archive_path):
    """Make .tgz file"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        li = archive_path.split('/')
        file_name = li[-1]
        run(f'mkdir -p /data/web_static/releases/{file_name[:-4]}')
        run(f'tar -xzf /tmp/{file_name} -C /data/web_static/releases/{file_name[:-4]}/')
        run(f'rm /tmp/{file_name}')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{file_name[:-4]}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception as e:
        return False

#!/usr/bin/python3
"""This is our model"""
from fabric.decorators import task
from fabric.operations import local
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['100.25.164.203', '54.90.3.135']


@task
def do_pack():
    """pack html files"""
    if not os.path.exists('versions'):
        os.mkdir('versions')
    current_datetime = datetime.now()
    fdt = current_datetime.strftime("%Y%m%d%H%M%S")
    cmd = 'tar -cvzf versions/web_static_{}.tgz web_static'.format(fdt)
    result = local(cmd)
    if result:
        return(os.path.abspath('versions'))
    return (None)


@task
def do_deploy(archive_path):
    """deploy archive file"""
    if not os.path.exists(archive_path):
        return(False)
    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split("/")[1].split(".tgz")[0]
        cmd1 = 'tar -xzf /tmp/{}.tgz -C /data/web_static/releases\
                /{}/'.format(filename, filename)
        run('mkdir -p /data/web_static/releases/{}/'.format(filename))
        run(cmd1)
        run('rm /tmp/{}.tgz'.format(filename))
        run('mv /data/web_static/releases/{}/web_static/* /data/\
                web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static\
                /current'.format(filename))
        return(True)
    except Exception:
        return(False)

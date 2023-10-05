#!/usr/bin/python3
"""This is our model"""
from fabric.operations import local
import os
from datetime import datetime


def do_pack():
    """fab function"""
    if not os.path.exists('versions'):
        os.mkdir('versions')
    current_datetime = datetime.now()
    fdt = current_datetime.strftime("%Y%m%d%H%M%S")
    cmd = 'tar -cvzf versions/web_static_{}.tgz web_static'.format(fdt)
    result = local(cmd)
    if result:
        return(os.path.abspath('versions'))
    return (None)

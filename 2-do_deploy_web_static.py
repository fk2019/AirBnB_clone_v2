#!/usr/bin/python3
"""Distribute an archive to web servers
"""
from fabric.api import env, run, put
import os

env.hosts = ['34.232.69.25', '18.233.67.224']


def do_deploy(archive_path):
    """Return True if deployment is successful
       otherwise False
    """
    if not os.path.exists(archive_path):
        return False
    target = "/data/web_static/releases/"
    filename = archive_path.split('.')[0].split('/')[1]
    dest_path = target + filename
    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest_path))
        run('tar -xcvf /tmp/{}.tgz -C {}'.format(filename, dest_path))
        run('rm -f /tmp/{}.tgz'.format(filename))
        run('mv {}/web_static/* {}/'.format(dest_apth, dest_path))
        run('rm -rf {}/web_static'.format(dest_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest_path))
        return True
    except Exception:
        return False

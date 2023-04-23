#!/usr/bin/python3
"""Generate .tgz archive from web_static contents
"""
from fabric.api import local, env, run, put
from datetime import datetime

env.hosts = ['34.232.69.25', '18.233.67.224']


def do_pack():
    """Create versions folder and return archive path
    """
    local("mkdir -p versions")
    path = local("tar -cvzf versions/web_static_{}.tgz web_static".
                 format(datetime.now().strftime("%Y%m%d%H%M%S")), capture=True)
    if path:
        return path
    else:
        return None


def do_deploy(archive_path):
    """Return True if deployment is successful
       otherwise False
    """
    if not os.path.exists(archive_path):
        return False
    target = "/data/web_static/releases/"
    filename = archive_path.split('.')[0].split('/')[1]
    archive = archive_path.split('versions/')[1]
    dest_path = target + filename
    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest_path))
        run('sudo tar -xvf /tmp/{} -C {}/'.format(archive, dest_path))
        run('sudo rm -f /tmp/{}.tgz'.format(archive))
        run('sudo mv /data/web_static/releases/{}/web_static/* {}/'.
            format(filename, dest_path))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'.
            format(filename))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest_path))
        return True
    except Exception:
        return False


def deploy():
    """Create and distribute an archive to web servers
"""
    path = do_pack()
    result = do_deploy(path)
    return result

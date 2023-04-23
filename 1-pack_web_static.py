#!/usr/bin/python3
"""Generate .tgz archive from web_static contents
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create versions folder and return archive path
    """
    local("mkdir -p versions")
    path = local("tar -cvzf versions/web_static_{}.tgz web_static".
                 format(datetime.now().strftime("%Y%m%d%H%M%S")),
                        capture=True)
    if path:
        return path
    else:
        return None

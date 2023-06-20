#!/usr/bin/env python

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path


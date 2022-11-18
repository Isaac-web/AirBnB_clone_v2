#!/usr/bin/python3
"""A fabfile for automating deployments"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Zip all the file in the web static
    folder into a single file
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(timestamp)
    zipped = local("tar -cfvz {} web_static".format(file_path))

    if zipped.succeeded:
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """
        Transfer the archive to the server
    """
    if not archive_path:
        return False

    put(local_path=archive_path, remote_path="/tmp")
    run("tar -xfv /tmp/{} /data/web_static/release/".format(archive_path))
    sudo("rm -f /tmp/{}".format(archive_path))
    sudo("rm -f /data/web_static/current")
    run("ln -sf /data/web_static/current ")

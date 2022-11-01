#!/usr/bin/python3

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

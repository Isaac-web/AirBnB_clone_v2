#!/usr/bin/python3

from fabric.api import *


def do_pack():
    """
    Zip all the file in the web static
    folder into a single file
    """

    #make a path for versions
    local("mkdir -p versions")

    #create a path for the tar file tobe created
    timestamp = datetime.now().strfstring("%Y%m%d%H%M%S")
    path = "versions/web_static_{}".format(timestamp)

    
    zip_archive = local("tar -cfuz {} web_static".format(path))

    if zip_archive.succedded:
        return path
    else:
        return None
    





#!/usr/bin/python3

from fabric.api import *


def do_pack():
    """
    Zip all the file in the web static
    folder into a single file
    """

    path = (
            "versions",
            "web_static_<year><month><day><hour><minute><second>.tgz"
            )

    try:
        local("tar -cvzf versions/web_static_20170314233357.tgz web_static")
        return path
    except Exception as e:
        pass
    return None

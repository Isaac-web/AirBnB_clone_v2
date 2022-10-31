#!/usr/bin/python3

from fabric.api import *


def do_pack():
    """
    Zip all the file in the web static
    folder into a single file
    """
    path="versions/web_static_20170314233357.tgz"
    local("tar -cvzf versions/web_static_20170314233357.tgz web_static")

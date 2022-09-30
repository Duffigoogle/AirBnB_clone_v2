#!/usr/bin/python3
"""Generates a .tgz archive from the
contents of the web_static folder"""

from fabric.api import local
import datetime

def do_pack():
    """ Function to compress files i.e A Fabric script that
    generates a .tgz archive from the contents of the web_static """
    local("mkdir -p versions")
    date = datetime.datetime.now()
    date_format = date.strftime("%Y%m%d%H%M%S")
    result_archive = local("tar -cvzf versions/web_static_{}.tgz web_static"
                           .format(date_format))
    if result_archive.succeeded:
        return "versions/web_static_{}.tgz".format(date_format)
    else:
        return None

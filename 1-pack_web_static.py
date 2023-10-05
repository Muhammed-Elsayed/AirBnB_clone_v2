#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """creates archive file"""
    dt = datetime.utcnow()
    archive_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                                 dt.month,
                                                                 dt.day,
                                                                 dt.hour,
                                                                 dt.minute,
                                                                 dt.second)

    if local("mkdir -p versions").failed is True:
        return None
    if local("tar -cvzf {} web_static".format(archive_file)).failed is True:
        return None
    return archive_file

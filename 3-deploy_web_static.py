#!/usr/bin/python3
"""implementing packing and deploying together"""
import os
from fabric.api import local
from datetime import datetime
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ["18.204.7.111", "100.26.213.167"]


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


def do_deploy(archive_path):
    """upload the archive to the web server and unzip it"""
    if os.path.exists(archive_path):
        try:
            fileName = archive_path.split("/")[1].split(".")[0]
            archive = archive_path.split("/")[1]
            put(archive_path, "/tmp/")
            run("mkdir -p /data/web_static/releases/{}/".format(fileName))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/\
".format(archive, fileName))
            run("rm -rf /tmp/{}".format(archive))
            run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(fileName, fileName))
            run("rm -rf /data/web_static/releases/{}/web_static\
".format(fileName))
            run("sudo rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{} \
/data/web_static/current".format(fileName))
        except Exception:
            return False
        return True
    else:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)

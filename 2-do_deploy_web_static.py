#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy"""
import os
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ["18.204.7.111", "100.26.213.167"]


def do_deploy(archive_path):
    """upload the archive to the web server and unzip it"""
    if os.path.exists(archive_path):
        try:
            fileName = archive_path.split("/")[1].split(".")[0]
            archive = archive_path.split("/")[1]
            put(archive_path, "/tmp/")
            run("mkdir -p /data/web_static/releases/{}/".format(fileName))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                archive, fileName))
            run("rm -rf /tmp/{}".format(archive))
            run("mv /data/web_static/releases/{}/web_static/* "
                "/data/web_static/releases/{}/".format(fileName, fileName))
            run("rm -rf /data/web_static/releases/{}/web_static".format(
                fileName))
            run("sudo rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{} "
                "/data/web_static/current".format(fileName))
        except Exception:
            return False
        return True
    else:
        return False

#!/usr/bin/python3
"""deletes out-of-date archives, using the function do_clean"""
from fabric.api import *
import os


env.hosts = ["18.204.7.111", "100.26.213.167"]


def do_clean(number=0):
    """deletes outdated versions"""
    if int(number) == 1 or int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]

    with lcd("versions"):
        [local("rm -rf {}".format(d) for d in archives)]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [d for d in archives if "web_static_" in d]
        [archives.pop() for i in range(number)]
        [run("rm -rf {}".format(d) for d in archives)]

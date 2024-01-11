#!/usr/bin/python3
"""script that generates a .tgz archive
from the contents of the web_static folder"""
from fabric.api import local
import datetime
import os


def do_pack():
    """generates a .tgz archive"""
    version_dir = "./versions"
    if not os.path.isdir(version_dir):
        os.makedirs(version_dir)

    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(current_time)
    archive_path = os.path.join(version_dir, archive_name)

    local("tar -czvf {} web_static/*".format(archive_path))

    return archive_path

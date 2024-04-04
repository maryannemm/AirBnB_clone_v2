#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from the contents of the web_static folder"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the name of the archive based on the current timestamp
    time_format = "%Y%m%d%H%M%S"
    archive_name = "versions/web_static_{}.tgz".format(datetime.now().strftime(time_format))

    # Compress the contents of the web_static folder into the archive
    result = local("tar -cvzf {} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result.failed:
        return None
    else:
        return archive_name


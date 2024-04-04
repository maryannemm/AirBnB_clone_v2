#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers and deploy it.
"""

from fabric.api import env, run
from fabric.operations import put
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # or your SSH username
env.key_filename = ['/path/to/your/ssh/private/key']  # specify your SSH private key


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    try:
        time_format = "%Y%m%d%H%M%S"
        archive_name = "versions/web_static_{}.tgz".format(datetime.now().strftime(time_format))

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name

    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.split(".")[0]
        dest_folder = "/data/web_static/releases/{}/".format(archive_no_ext)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(dest_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, dest_folder))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}".format(dest_folder, dest_folder))
        run("rm -rf {}web_static".format(dest_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_folder))

        return True

    except Exception as e:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers and deploys it.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)


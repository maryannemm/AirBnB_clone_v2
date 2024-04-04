#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives.
"""

from fabric.api import env, run, local, lcd
from datetime import datetime
from os.path import exists
from operator import itemgetter

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # or your SSH username
env.key_filename = ['/path/to/your/ssh/private/key']  # specify your SSH private key


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """

    try:
        if int(number) < 1:
            number = 1

        with lcd("versions"):
            local_archives = local("ls -1t | grep 'web_static_.*\.tgz'", capture=True).split("\n")

            if len(local_archives) > int(number):
                for i in range(int(number), len(local_archives)):
                    local("rm -f {}".format(local_archives[i]))

        with lcd("/data/web_static/releases"):
            run_archives = run("ls -1t | grep 'web_static_.*\.tgz'").split("\n")

            if len(run_archives) > int(number):
                run_archives = sorted(run_archives, key=lambda x: datetime.strptime(x.split('_')[2], "%Y%m%d%H%M%S"),
                                      reverse=True)
                for i in range(int(number), len(run_archives)):
                    run("rm -f {}".format(run_archives[i]))

        return True

    except Exception as e:
        return False


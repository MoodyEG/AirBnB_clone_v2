#!/usr/bin/python3
""" Main
Usage:
fab -f 100-clean_web_static.py do_clean:number=2 -i
my_ssh_private_key -u ubuntu > /dev/null 2>&1
"""
from fabric.api import local, env, put, run  # type: ignore


env.hosts = ['52.23.178.135', '100.25.47.15']


def do_clean(number=0):
    """ DELETE """
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1
    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(path, number))

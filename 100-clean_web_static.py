#!/usr/bin/python3
"""This module defines the function do_clean
"""
from fabric.api import *


env.hosts = ['52.23.178.135', '100.25.47.15']
env.user = 'ubuntu'


def do_clean(number=0):
    """This function deletes out-of-date archives
    """
    output = local("ls -lt ./versions/", capture=True)
    output = output.split('\n')
    output.pop(0)
    number = int(number)
    if number == 0:
        number = 1
    i = number
    while i <= (len(output) - 1):
        filename = output[i].split(' ')[-1]
        local("rm -rf ./versions/{}".format(filename))
        i += 1

    output = run("ls -lt /data/web_static/releases")
    output = output.split('\n')
    output.pop(0)
    print(output)
    i = int(number)
    while i <= (len(output) - 1):
        filename = output[i].split(' ')[-1]
        sudo("rm -rf /data/web_static/releases/{}".format(filename))
        i += 1


#!/usr/bin/python2
"""module to use hadoop to download a file"""
from snakebite.client import Client


def download(l):
    """method to download a file w/ hadoop"""
    client = Client('localhost', 9000)

    for f in client.copyToLocal(l, '/tmp'):
        if f['result']:
            print("File Downloaded: {}".format(f['path']))
        else:
            print("File Not Downloaded: '{}': {}".format(f['path'],
                                                         f['error']))

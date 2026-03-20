#!/usr/bin/python2
"""module for using snakebite with hadoop"""
from snakebite.client import Client

def deletedir(l):
    """method that deletes the directories listed on l within HDFS"""
    client = Client('localhost', 9000)
    l = sorted(l, reverse=True)
    for d in client.delete(l, recurse=True):
        if d['result']:
            print("Directory deleted: {}".format(d['path']))
        else:
            print("Failed to delete directory '{}': {}".format(d['path'], d['error']))
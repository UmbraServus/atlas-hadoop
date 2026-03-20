#!/usr/bin/python2
"""module for using snakebite with hadoop"""
from snakebite.client import Client

def createdir(l):
    """method that creates the directories listed on l within HDFS"""
    client = Client('localhost', 9000)

    for d in client.mkdir(l, create_parent=True):
        if d['result']:
            print("Directory created: {}".format(d['path']))
        else:
            print("Failed to create directory '{}': {}".format(d['path'], d['error']))
#!/usr/bin/env bash
# creates the directories /holbies and /holbies/input within HDFS.

hdfs dfs -mkdir -p /holbies
hdfs dfs -mkdir -p /holbies/input

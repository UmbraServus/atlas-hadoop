#!/usr/bin/python2
"""Mapper gets id, company and totalyearlycompensation from salaries.csv"""
import sys
import csv
header = None
reader = csv.reader(sys.stdin)
for fields in reader:
    if header is None:
        header = {col: idx for idx, col in enumerate(fields)}
        continue
    try:
        id = fields[header["id"]]
        company = fields[header["company"]]
        totalyearlycompensation = fields[header["totalyearlycompensation"]]
    except IndexError:
        continue

    print("{}\t{},{}".format(id, company, totalyearlycompensation))

#!/usr/bin/python2
"""takes the output of the mapper.py script and gives the top ten salaries
sorted by totalyearlycompensation"""
import sys


def get_salary(entry):
    return entry[0]

top10 = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    company, totalyearlycompensation = value.split(',', 1)

    try:
        salary = int(totalyearlycompensation)
    except ValueError:
        continue

    top10.append((salary, key, company))
    top10.sort(key=get_salary, reverse=True)

    if len(top10) > 10:
        top10.pop()

for salary, id, company in top10:
    print("{}\t{},{}".format(id, salary, company))

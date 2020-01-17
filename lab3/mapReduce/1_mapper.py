#!/usr/bin/python2

import sys

for line in sys.stdin:
    team_id = ""
    values = []
    line = line.strip().split(",")
    if len(line) == 2:
        team_id = line[0]
        key = team_id
        for token in line:
            values.append(token)
        print key + "\t" + str(values)


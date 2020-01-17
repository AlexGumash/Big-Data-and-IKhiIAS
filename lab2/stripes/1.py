#!/usr/bin/python2

import sys

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token:
            d = {}
            for token2 in line.strip().split(" "):
                if token != token2:
                    if d.get(token2):
                        d[token2] += 1
                    else:
                        d[token2] = 1
        print token + "\t" + str(d)


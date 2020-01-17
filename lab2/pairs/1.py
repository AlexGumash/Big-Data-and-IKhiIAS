#!/usr/bin/python2

import sys

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token:
            for token2 in line.strip().split(" "):
                if token != token2:

                    key = token + ',' + token2
                    print key + '\t1'

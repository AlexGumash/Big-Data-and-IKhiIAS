#!/usr/bin/python2
import sys, ast

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    print key + "\t" + value
    



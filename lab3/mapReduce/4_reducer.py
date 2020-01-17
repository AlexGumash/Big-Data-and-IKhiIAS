#!/usr/bin/python2
import sys, ast

(lastKey, output) = (None, [])

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print lastKey + '\t' + str(output)
        (lastKey, output) = (key, [ast.literal_eval(value)])
    else:
        output.append(ast.literal_eval(value))
        lastKey = key

if lastKey:
    print lastKey + '\t' + str(output)
    



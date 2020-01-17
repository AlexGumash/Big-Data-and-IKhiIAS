#!/usr/bin/python2
import sys
import json, ast

(lastKey, d)=(None, "{}")

def merge_to_dict(x, y):
    z = x.copy()
    for i in y:
        if z.get(i):
            z[i] += y[i]
        else:
            z[i] = y[i]
    return z

for line in sys.stdin:
    (key, dictationary) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print lastKey + '\t' + str(d)
        (lastKey, d) = (key, str(dictationary))
    else:
        a = json.loads(str(d).replace("'", "\""))
        b = json.loads(str(dictationary).replace("'", "\""))
        kek = merge_to_dict(a, b)
        kek = ast.literal_eval(json.dumps(kek))
        lastKey = key
        d = kek
#
if lastKey:
    print lastKey + '\t' + str(d)


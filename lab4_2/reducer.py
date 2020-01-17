#!/usr/bin/python3

import sys

last_key, links, weight_hub, weight_auth = None, [], 0, 0
for line in sys.stdin:
    key, values, label = line.rstrip().split('\t')
    # print(key, values, label)
    if last_key and last_key != key:
        print(f'{last_key}\t({",".join(links)});{weight_auth};{weight_hub}')
        if '(' in values:
            links = [values[1:-1]]
            weight_hub = 0
            weight_auth = 0
        else:
            links = []
            if label == 'hub':
                weight_hub = int(values)
            else:
                weight_auth = int(values)
        last_key = key
    else:
        if '(' in values:
            links.append(values[1:-1])
        else:
            if label == 'hub':
                weight_hub += int(values)
            else:
                weight_auth += int(values)
        last_key = key

if last_key:
    print(f'{last_key}\t({",".join(links)});{weight_auth};{weight_hub}')

#!/usr/bin/python3

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    links, weight_hub, weight_auth = values.split(';')
    for link in links[1:-1].split(','):
        print(f'{link}\t({key})\tlink')
        print(f'{link}\t{weight_hub}\tauth')
        # print(f'{key}\t({link})')
        print(f'{key}\t{weight_auth}\thub')
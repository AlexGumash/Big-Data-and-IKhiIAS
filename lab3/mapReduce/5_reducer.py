#!/usr/bin/python3
import sys, ast

lastKey = None
H = {}
H['cars'] = []
H['teams'] = []
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    key = int(key)
    value = eval(value)

    if lastKey and lastKey != key:
        for team in H['teams']:
            for car in H['cars']:
                print(str(team['team_name']) + "\t" + str(car))
        H = {}
        H['cars'] = []
        H['teams'] = []
        if value['table'] == 'cars':
            H['cars'].append(value)
        lastKey = key

    else:
        if value['table'] == 'cars':
            H['cars'].append(value)
        if value['table'] == 'teams':
            H['teams'].append(value)
        lastKey = key

if lastKey:
    for team in H['teams']:
        for car in H['cars']:
            print(str(team['team_name']) + "\t" + str(car))



#!/usr/bin/python3
import sys

for line in sys.stdin:
    lst = []
    dict = {}
    key = ''
    if line.find('|') != -1:
        lst = line.strip().split("|")
        key = lst[0]
        dict['table'] = 'teams'
        dict['team_name'] = lst[1]
    if line.find('/') != -1:
        lst = line.strip().split("/")
        key = lst[2]
        dict['table'] = 'cars'
        dict['car_name'] = lst[1]
        dict['car_team'] = lst[2]
        dict['car_year'] = lst[3]
    if dict:
        print(str(key) + '\t' + str(dict))




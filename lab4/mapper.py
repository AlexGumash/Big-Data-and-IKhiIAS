#!/usr/bin/python3

import sys

for line in sys.stdin:
    key, values = line.rstrip().split(';')
    # graph, auth_hub = values.split(';')
    # print(key + '\t' + str(graph[1:-1].split(',')))
    for edge in key[1:-1].split(','):
        # Для каждого ребра выводить ребро и вершину,
        # чтобы получить транспонированный граф.
        print(edge + '\t' + key)
        # Для каждого ребра выводить ребро и его
        # оценку авторитетности или посредническую оценку.
        print(edge + '\t' + values)
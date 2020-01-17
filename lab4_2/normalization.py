#!/usr/bin/python3
import pyhdfs
import sys

fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='bsbo228')
output = fs.open(f'/user/bsbo228/lab4/stage{sys.argv[1]}/part-00000')

norm_sum = 0
for line in output:
    key, value = line.decode().strip().split("\t")
    weight = int(value.split(';')[1])
    norm_sum += weight

output = fs.open(f'/user/bsbo228/lab4/stage{sys.argv[1]}/part-00000')
for line in output:
    key, value = line.decode().strip().split("\t")
    weight = int(value.split(';')[1])
    weight = float("{0:.2f}".format(weight/norm_sum))
    print(key + ' - ' + str(weight))

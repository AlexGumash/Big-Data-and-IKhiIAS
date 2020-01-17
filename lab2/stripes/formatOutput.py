#!/usr/bin/python2
import pyhdfs
import ast, json

word = str(input("Your word: "))
count = int(input("Count: "))

fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='bsbo228')
output = fs.open('/user/bsbo228/lab2/output/part-00000')

for line in output:
    striped = line.strip().split("\t")
    key = striped[0].split(',')[0]
    d = striped[1]
    d = json.loads(d.replace("'", "\""))
    d = ast.literal_eval(json.dumps(d))
    if key == word:
        list_d = list(d.items())
        list_d.sort(key=lambda i: i[1], reverse=True)
        j = 0
        print (str(count) + " most purchased items with item " + word)
        for i in list_d:
            if j < count:
                print str(i[0])+': ' + str(i[1])
            j += 1
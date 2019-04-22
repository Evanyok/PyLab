import os
import pandas as pd
import json

print(os.getcwd())

print(os.path.abspath(os.pardir))

print(os.path.abspath(__file__))

with open('test.txt', mode='r') as fo:
    lines = fo.readlines()
    for line in lines:
        print(line.strip())

test =  pd.read_csv('test.csv')
with open('header.txt', mode='w+') as hw:
    for line in test.columns:
        print(line)
        hw.write(line.strip() + '\n')

x = dict(height=111, weight=222)
y = json.dumps(x)
print(y) # serialized
x = json.loads(y)
print(x) # unserialized
with open('test.json', mode="w") as jw:
    json.dump(x, jw)
with open('test.json', mode="r") as jr:
    print(json.load(jr))
import copy
import numpy as np
import os

os.chdir("_adventofcode/adventofcode2021/6")

with open("input.txt", 'r') as f:
    d = f.readline().split(',')
    data = []
    for i in d:
        data.append(int(i))

days = 256

"""
for i in range(0,days):
    new = 0
    for j in range(0,len(data)):
        if data[j] == 0:
            data[j] = 6
            new += 1
        else:
            data[j] -= 1
    for i in range(0,new):
        data.append(8)

print(len(data))
"""
#1909 incorrect



# how many are at x days
numpd = [0,0,0,0,0,0,0,0,0]
for j in range(0,len(data)):
    numpd[data[j]] += 1

for i in range(0,days):
    new = numpd[0]
    for j in range(1,len(numpd)):
        numpd[j-1] = numpd[j]
    numpd[8] = new
    numpd[6] += new

print(sum(numpd))
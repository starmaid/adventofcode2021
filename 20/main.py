import copy
import numpy as np
import os
import math as m

os.chdir("adventofcode2021/20")

with open("input.txt", 'r') as f:
    alg = f.readline().strip('\n').replace('#','1').replace('.','0')
    f.readline()
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n').replace('#','1').replace('.','0'))

print(alg)

[print(d) for d in data]

s = 0
for r in data:
    s += r.count('1')
print(s)

def getp(arr,x,y,r):
    if r % 2 == 0:
        defa = '0'
    else:
        defa = alg[0].replace('#','1')
    
    if (x < 0) or (x >= len(arr[0])):
        out = defa
    elif (y < 0) or (y >= len(arr)):
        out = defa
    else:
        out = arr[y][x]
    return out

def getsurr(arr,x,y,r):
    outs = ''
    for i in range(-1,2):
        for j in range(-1,2):
            outs += getp(arr,x+j,y+i,r)
    return outs

for r in range(0,50):
    ndata = []
    for y in range(-1,len(data)+1):
        line = ''
        for x in range(-1,len(data[0])+1):
            outv = int(getsurr(data,x,y,r),base=2)
            line += alg[outv]
        ndata.append(line)
    
    data = copy.deepcopy(ndata)
    [print(d) for d in data]
    s = 0
    for r in data:
        s += r.count('1')
    print(s)


#10609 too high
#5617 too high

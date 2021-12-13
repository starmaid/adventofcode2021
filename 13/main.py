import copy
import numpy as np
import os
import re

os.chdir("adventofcode2021/13")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    inst = []
    for i in d:
        if re.match(r'[0-9,]+',i):
            data.append([int(x) for x in i.strip('\n').split(',')])
        else:
            if i != '\n':
                inst.append(i.split(' ')[-1].strip('\n').split('='))
            
points = np.array(data)
#print(points)
#print(inst)

height = np.max(points[:,1])
width = np.max(points[:,0])
#print(str(height) + " " + str(width))

dots = np.zeros((height + 1,width + 1),dtype=int)
#print(dots)

# add dots to array
for p in points:
    dots[p[1],p[0]] = 1

print(dots)

# fold
for f in inst:
    if f[0] == 'y':
        liney = int(f[1])
        # for all rows below y = liney
        for y in range(liney+1,len(dots)):
            for x in range(0,len(dots[y,:])):
                if dots[y,x] == 1:
                    dots[liney - (y-liney),x] = 1
        dots = dots[0:liney]
    elif f[0] == 'x':
        linex = int(f[1])
        # for all cols below x = linex
        for x in range(linex+1,len(dots[0,:])):
            for y in range(0,len(dots)):
                if dots[y,x] == 1:
                    dots[y,linex - (x-linex)] = 1
        dots = dots[:,0:linex]

print(str(dots))

n = np.count_nonzero(dots == 1)
print(n)
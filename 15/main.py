import copy
import numpy as np
import os

os.chdir("adventofcode2021/15")

with open("input1.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append([int(c) for c in i.strip('\n')])

startpos = 0,0
endpos = len(data),len(data)

data = np.array(data)
dist = np.zeros((len(data),len(data)),dtype=np.int64)
dist[:,:] = 999999
dist[startpos] = 0
prev = np.zeros((len(data),len(data),2),dtype=np.int64)
prev[:,:,:] = -1
Q = {}


for x in range(0,len(data)):
    for y in range(0,len(data)):
        Q["{},{}".format(x,y)] = dist[y,x]

Q.sort()

print(data)

# weighted graph shortest path





def getlength(data,x,y):
    if not (0 < x < len(data)) or not (0 < x < len(data)):
        return None
    else:
        return data[y,x]


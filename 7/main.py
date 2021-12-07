import copy
import numpy as np
import os

os.chdir("adventofcode2021/7")

with open("input.txt", 'r') as f:
    d = f.readline().split(',')
    data = []
    for i in d:
        data.append(int(i))

# bring every ship to position 0
# bring every ship to position max(data)
# calculate fuel, store in an array size of that
moves = np.zeros(len(data),dtype=int)
fuel = np.zeros(max(data),dtype=int)

for i in range(0,max(data)):
    for d in range(0,len(data)):
        m = abs(data[d]-i)
        moves[d] = m
        fuel[i] += m * (m+1) / 2

pos = np.where(fuel==min(fuel))[0][0]

print(pos)
print(fuel[pos])
import copy
from typing import final
import numpy as np
import os

os.chdir("adventofcode2021/14")

with open("input.txt", 'r') as f:
    d = f.readline()
    templ = d.strip('\n')
    f.readline()
    d = f.readlines()
    data = {}
    for i in d:
        f = i.strip('\n').split(' -> ')
        data[f[0]] = f[1]

print(templ)
print(data)

begchar = templ[0]
endchar = templ[-1]

# setup
def setempty(rules):
    out = {}
    for f in rules:
        out[f] = 0
    return out

rulesn = setempty(data.keys())
print(rulesn)

p = 0
for p in range(0, len(templ) - 1):
    rulesn[templ[p:p+2]] += 1

print(rulesn)

for t in range(0,40):
    nrulesn = setempty(data.keys())
    for k in rulesn.keys():
        # add that number to the two spawned ones
        nrulesn[k[0] + data[k]] += rulesn[k]
        nrulesn[data[k] + k[1]] += rulesn[k]
        
    rulesn = nrulesn

# find final numbers
finalscore = setempty([data[k] for k in data.keys()])
for k in rulesn.keys():
    finalscore[k[0]] += rulesn[k]
    finalscore[k[1]] += rulesn[k]

for s in finalscore.keys():
    if s == begchar or s == endchar:
        finalscore[s] = (finalscore[s] + 1) / 2
    else:
        finalscore[s] /= 2

print(finalscore)

sc = [finalscore[k] for k in finalscore.keys()]

s = max(sc) - min(sc)
print(s)


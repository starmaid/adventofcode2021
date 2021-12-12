import copy
import numpy as np
import os
import re

os.chdir("adventofcode2021/12")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n').split('-'))

class cave:
    def __init__(self,a,b):
        self.name = a
        if re.match(r"[A-Z]+",self.name):
            self.big = True
        else:
            self.big = False
        self.adj = [b]
        self.visited = False
    
    def __str__(self):
        return("{} {} {}".format(self.name,self.big,self.adj))

caves = {}

# go through and build the list
for d in data:
    if d[0] in caves.keys():
        caves[d[0]].adj.append(d[1])
    else:
        a = cave(d[0],d[1])
        caves[d[0]] = a

    if d[1] in caves.keys():
        caves[d[1]].adj.append(d[0])
    else:
        a = cave(d[1],d[0])
        caves[d[1]] = a


for i in caves:
    print(caves[i])

# find the path

def clear():
    global caves
    for k in caves.keys():
        caves[k].visited = False

routes = []

# BFS

def BFS(start,end,path,twice):
    npath = copy.deepcopy(path)
    npath.append(start.name)
    if start.name == end.name:
        global routes
        routes.append(npath)
        return

    global caves
    for a in start.adj:
        c = caves[a]
        if c.big or (a not in path):
            BFS(c,end,npath,twice)
        else:
            if a == twice and path.count(a) < 2:
                BFS(c,end,npath,twice)
    return

BFS(caves['start'],caves['end'],[],'')

for v in caves.keys():
    if v != 'start' and v != 'end' and re.match(r"[a-z]+",v):
        BFS(caves['start'],caves['end'],[],v)

print("removing duplicates")
# remove duplicates
r = 0
while r < len(routes):
    s = routes[r]
    c = routes.count(s)
    if c == 1:
        r += 1
    else:
        for x in range(0,c):
            routes.remove(s)
        routes.append(s)
    print("\r" + str(len(routes)),end='')

for r in routes:
    print("{} {}".format(r,routes.count(r)))

print(len(routes))
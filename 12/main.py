import copy
import numpy as np
import os

os.chdir("12")

with open("input1.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n').split('-'))

class cave:
    def __init__(self,a,b):
        self.head = a
        self.tail = [b]
        self.visited = False
    
    def __str__(self):
        return("{} {}".format(self.head,self.tail))

caves = []

# go through and build the list
for i in data:
    done = False
    for c in caves:
        if i[0] == c.head:
            c.tail.append(i[1])
            done = True
    if not done:
        a = cave(i[0],i[1])
        caves.append(a)

for i in caves:
    print(i)


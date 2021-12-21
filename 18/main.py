import copy
import numpy as np
import os
import math as m

os.chdir("adventofcode2021/18")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n'))

print(data)

# lmao mark just suggested doing a flat list

#read line into array and depth list

NUMBERS = '1234567890'

def parseline(s):
    global NUMBERS
    deps = []
    vals = []
    p = 0
    d = -1
    mem = ''
    while p < len(s):
        # parse the char
        if s[p] == '[':
            d += 1
        elif s[p] == ']':
            if mem != '':
                vals.append(int(mem))
                deps.append(d)    
                mem = ''
            d -= 1
        elif s[p] in NUMBERS:
            mem += s[p]
        elif s[p] == ',':
            if mem != '':
                vals.append(int(mem))
                deps.append(d)    
                mem = ''
        p += 1

    return vals,deps


# start part 1! have to redefine things for part 2
vals,deps = parseline(data[0])

print(vals)
print(deps)



'''
for i in range(1,len(data)):
    nvals,ndeps = parseline(data[i])
    vals = vals + nvals
    deps = deps + ndeps
    deps = [x+1 for x in deps]

    done = False

    while not done:
        p = 0
        # go along and explode em
        while p < len(vals):
            if deps[p] > 3:
                # we know we have to explode two numbers
                # add to left
                # add to right
                # both numbers are replaced by a 0 at depth d-1

                if p > 0:
                    vals[p-1] += vals[p]
                if p+2 < len(vals):
                    vals[p+2] += vals[p+1]
                
                vals.pop(p+1)
                deps.pop(p+1)
                vals[p] = 0
                deps[p] = deps[p] - 1
            p += 1
        
        # now we go through and splits
        p = 0
        while p < len(vals):
            if vals[p] > 9:
                v = vals[p]/2
                vals[p] = m.floor(v)
                deps[p] += 1

                vals.insert(p+1,m.ceil(v))
                deps.insert(p+1,deps[p])
                
                #now go back and do the explodes
                break
            else:
                p += 1
                if p == len(vals):
                    done = True
'''

print(vals)
print(deps)


# get magnitude
while len(vals) > 1:
    for d in range(3,-1,-1):
        i = 0
        while i < len(vals):
            if deps[i] == d:
                vals[i] = 3*vals[i] + 2*vals[i+1]
                deps[i] -= 1
                vals.pop(i+1)
                deps.pop(i+1)
            
            i += 1


print(vals)


def simplify(vals,deps,nvals,ndeps):
    vals = vals + nvals
    deps = deps + ndeps
    deps = [x+1 for x in deps]

    done = False

    while not done:
        p = 0
        # go along and explode em
        while p < len(vals):
            if deps[p] > 3:
                # we know we have to explode two numbers
                # add to left
                # add to right
                # both numbers are replaced by a 0 at depth d-1

                if p > 0:
                    vals[p-1] += vals[p]
                if p+2 < len(vals):
                    vals[p+2] += vals[p+1]
                
                vals.pop(p+1)
                deps.pop(p+1)
                vals[p] = 0
                deps[p] = deps[p] - 1
            p += 1
        
        # now we go through and splits
        p = 0
        while p < len(vals):
            if vals[p] > 9:
                v = vals[p]/2
                vals[p] = m.floor(v)
                deps[p] += 1

                vals.insert(p+1,m.ceil(v))
                deps.insert(p+1,deps[p])
                
                #now go back and do the explodes
                break
            else:
                p += 1
                if p == len(vals):
                    done = True
    return vals,deps




for i in range(1,len(data)):
    nvals,ndeps = parseline(data[i])
    vals,deps = simplify(vals,deps,nvals,ndeps)


def getmag(vals,deps):
    while len(vals) > 1:
        for d in range(3,-1,-1):
            i = 0
            while i < len(vals):
                if deps[i] == d:
                    vals[i] = 3*vals[i] + 2*vals[i+1]
                    deps[i] -= 1
                    vals.pop(i+1)
                    deps.pop(i+1)
                i += 1
    return vals[0]


print(getmag(vals,deps))


#part 2!
# re parse the data into a massive array
# get the mag of one
# mag of their sum is 3*f+2*s

alllines = []
for i in range(0,len(data)):
    vals,deps=parseline(data[i])
    alllines.append([vals,deps])

print(alllines)

maxv = 0

for i in range(0,len(data)):
    for j in range(0,len(data)):
        if i == j:
            continue
        else:
            v,d = simplify(alllines[i][0],alllines[i][1],alllines[j][0],alllines[j][1])
            maxt = getmag(v,d)
            if maxt > maxv:
                maxv = maxt

print(maxv)






'''
my first thought was to start representing 
this all as objects with methods yknow

instead i might just do some string operations
sounds....easier to debug

lets hope part 2 isnt that bad

note: 


class pair():
    def __init__(self,parent,left=None,right=None):
        self.parent = parent
        self.left = left
        self.right = right
        
        if parent = None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
    
    def addleft(self,val):
        if isinstance(self.left, list):

    
    def explode(self):
'''





'''
s = ''
NUMBERS = '1234567890'

for i in range(1,2):
    s = '[' + data[i-1] + ',' + data[i] + ']'
    print(s)

    # go through once and do the 


def fullexplode(s):
    # fully explodes this number
    p = 0
    d = 0
    right = None
    left = None
    while p < len(s):
        # parse the char
        if s[p] == '[':
            d += 1
        elif s[p] == ']':
            d -= 1
        


        p += 1

'''



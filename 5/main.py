import copy
import numpy as np

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        w = i.strip('\n')
        ab = w.split(' -> ')[0].split(',')
        cd = w.split(' -> ')[1].split(',')
        data.append([int(ab[0]),int(ab[1]),int(cd[0]),int(cd[1])])

#data = [[[a,b,c,d]],
data = np.array(data, dtype=int)
m = np.max(data[:,:])+1
field = np.zeros((m,m), dtype=int)
#field = np.zeros((10,10), dtype=int)

for l in data:
    #print(l)
    if l[0] != l[2] and l[1] != l[3]:
        diagonal = True
    else:
        diagonal = False
    
    
    if l[0] > l[2]:
        stepx = -1
    else:
        stepx = 1
    
    if l[1] > l[3]:
        stepy = -1
    else:
        stepy = 1
    
    for x in range(l[0], l[2]+stepx, stepx):
        for y in range(l[1], l[3]+stepy, stepy):
            if diagonal:
                if stepx*(x-l[0]) != stepy*(y-l[1]):
                    #print("{} ignore {} {}".format(l,x-l[0],y-l[1]))
                    continue
            field[y,x] += 1
            #print("{} {} {}".format(l,x,y))

count = 0

for i in field:
    for j in i:
        if j > 1:
            count += 1

#1527 wrong
print(count)
#7142 correct

#13725 wrong


"""
for l in data:
    #print(l)
    if l[0] != l[2] and l[1] != l[3]:
        #print(l)
        continue
    
    if l[0] > l[2] or l[1] > l[3]:
        step = -1
        #print('backwards')
    else:
        step = 1
    
    for x in range(l[0], l[2]+step, step):
        for y in range(l[1], l[3]+step, step):
            field[y,x] += 1
            #print("{} {} {}".format(l,x,y))
"""
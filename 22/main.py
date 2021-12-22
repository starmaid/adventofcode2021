import copy
import numpy as np
import os
import math as m

os.chdir("adventofcode2021/22")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        out = []
        a,b = i.split(' ')
        if a == 'on':
            out.append([1,0])
        else:
            out.append([0,0])
        
        for v in b.split(','):
            out.append([int(x) for x in v.split('=')[1].split('..')])
        
        data.append(out)
    
print(data)

data = np.array(data)


# we cant store the entire area
# we ALSO cant store every lit cube
# maybe we can store ranges of lit cubes?

vol = 0

for i in range(0,len(data)):
    x0 = []
    x1 = []
    for k in range(1,4):
        x0.append(data[i][k][0])
        x1.append(data[i][k][1])
    
    #build point cloud of i
    psi = []
    for x in range(x0[0],x1[0]+1):
        for y in range(x0[1],x1[1]+1):
            for z in range(x0[2],x1[2]+1):
                psi.append('{},{},{}'.format(x,y,z))
    
    # LIST OF CUBES THAT ARE ALREADY ON
    ons = []

    # go through all previously calculated cubez
    for j in range(0,i):
        inter = False
        k = 0
        while True:
            if k == 3:
                inter = True
                break
            bx0 = data[j][k+1][0]
            bx1 = data[j][k+1][1]
            if (x0[k] <= bx0 <= x1[k]) or (x0[k] <= bx1 <= x1[k]) \
                or (bx0 <= x0[k] <= bx1) or (bx0 <= x1[k] <= bx1):
                #then theres the possibility of an intersection
                k += 1
            else:
                break
                
        if inter:
            #then theres an intersection
            # and we have to subtract the number in common
            print('inter {} {}'.format(i,j))

            #build point cloud of j
            bx0 = []
            bx1 = []
            for k in range(1,4):
                bx0.append(data[j][k][0])
                bx1.append(data[j][k][1])
            psj = []
            for x in range(bx0[0],bx1[0]+1):
                for y in range(bx0[1],bx1[1]+1):
                    for z in range(bx0[2],bx1[2]+1):
                        psj.append('{},{},{}'.format(x,y,z))

            inters = np.intersect1d(psi,psj)
            # if this set turned em on already, then we
            if data[j][0][0] == 1:
                ons = np.union1d(ons,inters)
            else:
                ons = np.setdiff1d(ons,inters)
    
    if data[i][0][0] == 1:
        # turn on all these
        newvol = len(psi) - len(ons)
        print(newvol)
        vol += newvol
    else:
        subvol = len(ons)
        print(subvol)
        vol -= subvol
    
    print('total: {}'.format(vol))

print(vol)

        

# check all precious vals for intersection
# no intersection? just add vol
# generate point cloud if theres an intersection
# do union math
# add/subtract that vol
















'''
# wow who woulda thought
# numpy.core._exceptions.MemoryError: Unable to allocate 951. TiB for an array with shape (77545, 166235, 81132) and data type bool

data = np.array(data)
maxx = np.max(data[:,1,1])
minx = abs(np.min(data[:,1,0]))
maxy = np.max(data[:,2,1])
miny = abs(np.min(data[:,2,0]))
maxz = np.max(data[:,3,1])
minz = abs(np.min(data[:,3,0]))

field = np.zeros((minx+maxx+1,miny+maxy+1,minz+maxz+1),dtype=bool)
#just add 50 to any coordinate operation

print(np.shape(field))

# now turn on cubes

for r in data:
    x0 = r[1][0] + minx
    x1 = (r[1][1]+1) + minx
    y0 = r[2][0] + miny
    y1 = (r[2][1]+1) + miny
    z0 = r[3][0] + minz
    z1 = (r[3][1]+1) + minz
    field[z0:z1,y0:y1,x0:x1] = r[0][0]


print(np.count_nonzero(field))
'''
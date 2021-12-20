import copy
import numpy as np
import os
from math import inf as INFINITY
from math import prod

os.chdir("adventofcode2021/16")

with open("input.txt", 'r') as f:
    d = f.readline().strip('\n')
    
# first turn it all into a string of binary characters
db = ''
for c in d:
    db += (str(bin(int(c,16))).split('0b')[1].zfill(4))

#print(db)

def packread(start,end=INFINITY,numpak=INFINITY):
    global db
    packets = []
    p = start
    npaks = 0
    while p < end and npaks < numpak:
        # assume a new packet starts here
        pak = {}
        cpackets = []
        pak['ver'] = int(db[p:p+3],base=2)
        p += 3
        pak['id'] = int(db[p:p+3],base=2)
        p += 3

        if pak['id'] == 4:
            v = ''
            while True:
                if db[p] == '1':
                    # not the last
                    v += db[p+1:p+5]
                    p += 5
                else:
                    # last one
                    v += db[p+1:p+5]
                    p += 5
                    break
            pak['val'] = int(v,base=2)
            
        else:
            # its an operator
            # contains sub packets
            pak['lentype'] = int(db[p])
            p += 1
            
            if pak['lentype'] == 0:
                # 15 bits of a total length of sub packets
                pak['subLength'] = int(db[p:p+15],base=2)
                p += 15
                p,pk = packread(p,end=(p+pak['subLength']))
                cpackets += pk

            elif pak['lentype'] == 1:
                # 11 bits of a total number of sub packets
                pak['subSize'] = int(db[p:p+11],base=2)
                p += 11
                p,pk = packread(p,numpak=pak['subSize'])
                cpackets += pk

            # now to do the math the operator desires
            cv = pak['id']
            opvals = [x['val'] for x in cpackets]
            if cv == 0:
                #sum
                pak['val'] = sum(opvals)
            elif cv == 1:
                #product
                pak['val'] = prod(opvals)
            elif cv == 2:
                # minimum
                pak['val'] = min(opvals)
            elif cv == 3:
                # max
                pak['val'] = max(opvals)
            elif cv == 5:
                # greater than
                if opvals[0] > opvals[1]:
                    pak['val'] = 1
                else:
                    pak['val'] = 0
            elif cv == 6:
                # less than
                print(p)
                if opvals[0] < opvals[1]:
                    pak['val'] = 1
                else:
                    pak['val'] = 0
            elif cv == 7:
                # equal
                if opvals[0] == opvals[1]:
                    pak['val'] = 1
                else:
                    pak['val'] = 0
            else:
                print('broken packet id -- freak out!!!!!')
        
        pak['children'] = cpackets
        packets.append(pak)
        npaks += 1

        # check if we might be at the end and eat some zeros
        if 0 < (len(db) - p) <= 7:
            while p < len(db):
                if db[p] == '0':
                    p += 1
                    #print('eat')
                else:
                    break
    
    
    return p, packets


p,packets = packread(0,len(db))

for p in packets:
    print(p)

#sver = 0
#for p in packets:
#    sver += p['ver']

#print(sver)
#1663 is wrong

print(packets[0]['val'])
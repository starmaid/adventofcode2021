import copy
import numpy as np
import os

os.chdir("adventofcode2021/8")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for l in d:
        m = l.strip('\n').split('|') # should have split by ' | ' instead to not have to FUCK around with the strip method. wasted like 5 min.
        d1 = m[0].strip(' ').split(' ')
        d2 = m[1].strip(' ').split(' ')
        data.append([d1,d2])

occ = 0
# part 1
for dis in data:
    for c in dis[1]:
        if len(c) == 2 or len(c) == 4 or len(c) == 3 or len(c) == 7:
            occ += 1

print(occ)

def add2(decoded, val):
    return decoded * 10 + val

bigsum = 0
alldecoded = []

for dis in data:
    cipher = ['','','','','','','']
    dis[0].sort(key=len)
    for c in dis[0]:
        l = len(c)
        if l == 2:
            # its a 1
            cipher[2] += c
            cipher[5] += c
        
        elif l == 3: 
            # its 7
            # only one that has pos0
            for char in c:
                if char not in cipher[2] and char not in cipher[5]:
                    cipher[0] = char
        
        elif l == 4:
            # its a 4
            # only one that has pos3
            for char in c:
                if char not in cipher[2] and char not in cipher[5]:
                    cipher[1] += char
                    cipher[3] += char
        
        elif l == 5:
            # 5 2 or 3
            pass

        elif l == 6:
            # 0 or 6 or 9
            # if it only has one of the right side chars, its 6
            if len(cipher[2]) == 2:
                if not (cipher[2][0] in c and cipher[2][1] in c):
                    for char in cipher[2]:
                        if char not in c:
                            cipher[5] = cipher[5].replace(char,'')
                            cipher[2] = char
            
            # if pos3 and pos1 arent both there, we know its 0
            if len(cipher[3]) == 2:
                if not (cipher[3][0] in c and cipher[3][1] in c):
                    for char in cipher[3]:
                        if char not in c:
                            cipher[1] = cipher[1].replace(char,'')
                            cipher[3] = char


        elif l == 7:
            #its 8
            pass

    decoded = 0
    
    for c in dis[1]:
        l = len(c)
        if l == 2:
            # its a 1
            decoded = add2(decoded,1)
        
        elif l == 3: 
            # its 7
            # only one that has pos0
            decoded = add2(decoded,7)

        
        elif l == 4:
            # its a 4
            # only one that has pos3
            decoded = add2(decoded,4)

        
        elif l == 5:
            # 5 2 or 3
            if cipher[2] in c and cipher[5] in c:
                # we know its 3
                decoded = add2(decoded,3)
                
            elif cipher[2] in c:
                # we know its 2
                decoded = add2(decoded,2)
                
            elif cipher[5] in c:
                # we know its 5
                decoded = add2(decoded,5)
                
        

        elif l == 6:
            # 0 or 6 or 9
            # if it only has one of the left side chars, its 6
            if not (cipher[2] in c and cipher[5] in c):
                decoded = add2(decoded,6) 
            elif cipher[3] not in c:
                decoded = add2(decoded,0)
            # if both pos3 and pos1 isnt there, we know its 0
            else:
                decoded = add2(decoded,9)

        elif l == 7:
            #its 8
            decoded = add2(decoded,8)
    
    bigsum += decoded
    alldecoded.append(decoded)


print(bigsum)
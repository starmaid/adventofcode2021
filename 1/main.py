

with open("input.txt", 'r') as f:
    data = f.readlines()
    data1 = []
    for i in data:
        data1.append(int(i.strip('\n')))

inc = 0
dec = 0

for i in range(0,len(data1)-1):
    i
    data1[i]
    data1[i+1]
    if data1[i+1] > data1[i]:
        inc += 1
    else:
        dec += 1


inc = 0
dec = 0

for i in range(0,len(data1)-3):
    #i
    #data1[i]
    #data1[i+1]
    if (data1[i+1] + data1[i+2] + data1[i+3]) > (data1[i] + data1[i+1] + data1[i+2]):
        inc += 1
    else:
        dec += 1
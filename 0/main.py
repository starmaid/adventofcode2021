with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        w = i.strip('\n')
        move = w.split(' ')[0]
        val = int(w.split(' ')[1])
        data.append([move, val])
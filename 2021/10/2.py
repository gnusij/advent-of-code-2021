import numpy as np

def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

seqs = [[str(i) for i in j] for j in read('input')]

lookup = {
    "(":")",
    "{":"}",
    "[":"]",
    "<":">",
}
plook = {
    ")":1,
    "]":2,
    "}":3,
    ">":4,
}

points = []
for seqt in seqs:
    point = 0
    seq = seqt
    while True:
        gind = []
        for i in range(len(seq)-1):
            try:
                if seq[i+1] == lookup[seq[i]]:
                    gind.append(i)
                    gind.append(i+1)
            except KeyError:
                continue
        #print(gind)
        if gind == []:
            break
        else:
            for i in gind[::-1]:
                _ = seq.pop(i)

    stop = False
    for i in range(len(seq)-1):
        if seq[i] in lookup.keys() and seq[i+1] in lookup.values():
            stop = True
            
    if not stop:
        req = []
        for i in seq[::-1]:
            req.append(lookup[i])

        for r in req:
            point = (point*5) + plook[r]

        points.append(point)
print(np.median(points))
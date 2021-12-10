import numpy as np

def read(file):
    with open(file, 'r') as f:
        return f.read()

seq = [str(i) for i in read('input')]
seq = list(filter(lambda x: x!='\n', seq))
#print(seq)

lookup = {
    "(":")",
    "{":"}",
    "[":"]",
    "<":">",
}

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
#if len(seq) != 0:
    #print(seq)

illegals = []

for i in range(len(seq)-1):
    if seq[i] in lookup.keys() and seq[i+1] in lookup.values():
        illegals.append(seq[i+1])

#print(illegals)

points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}

print(sum([points[i] for i in illegals]))
import numpy as np

def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()


def fold(inst, dots):
    new_dots = dots[:]

    axis = inst.split('=')[0][-1]
    if axis == "y":
        axis = 1
    else:
        axis = 0
    num  = int(inst.split('=')[1])

    for i,dot in enumerate(dots):
        if dot[axis] >= num:
            new_dots[i][axis] = num - abs(num - dot[axis])

    new_k = []
    for elem in new_dots:
        if elem not in new_k:
            new_k.append(elem)
    print("after", inst, "len:", len(new_k) )
    return new_k


dots = []
coms = []
inst = False

for line in read('input'):
    if line != "" and not inst:
        i, j = line.split(',')
        dots.append([int(i),int(j)])
    elif line == "":
        inst = True
    elif inst:
        coms.append(line)

print(dots)
print(coms)

for com in coms:
    dots = fold(com, dots)

print(dots)
print("A", len(dots))

import matplotlib.pyplot as plt

xs = []
ys = []

for dot in dots:
    xs.append(dot[0])
    ys.append(-1*dot[1])

plt.figure()
plt.scatter(xs, ys)
plt.grid()
plt.gca().set_aspect("equal")
plt.show()

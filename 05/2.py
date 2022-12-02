
import numpy as np
import pandas as pd
from collections import Counter

def read(file):
    with open(file, 'r') as f: return f.read().splitlines()

dangers = []
for i,inp in enumerate(read('input')):
    x1 = int(inp.split('->')[0].split(',')[0].strip())
    y1 = int(inp.split('->')[0].split(',')[1].strip())
    x2 = int(inp.split('->')[1].split(',')[0].strip())
    y2 = int(inp.split('->')[1].split(',')[1].strip())


    if x1 == x2:
        #print(x1,y1, 'to', x2,y2)
        for j in range(min([y1,y2]), max([y2,y1])+1):
            #print('adding ', (x1,j) )
            dangers.append( (x1,j) )
    elif y1 == y2:
        #print(x1,y1, 'to', x2,y2)
        for j in range(min([x1,x2]), max([x2,x1])+1):
            #print('adding ', (j,y1)  )
            dangers.append( (j,y1) )

    elif (y2-y1)/(x2-x1) == 1:
        x = min([x1, x2])
        y = min([y1, y2])
        while x < max([x1, x2])+1 and y < max([y1, y2])+1:
            dangers.append( (x,y) )
            x += 1
            y += 1

    elif (y2-y1)/(x2-x1) == -1:
        x = max([x1, x2])
        y = min([y1, y2])
        j = 0
        while x > min([x1, x2])-1 and y < max([y1, y2])+1:
            dangers.append( (x,y) )
            x -= 1
            y += 1


counter = 0
a = [item for item, count in Counter(dangers).items() if count > 1]
print(len(a))

import numpy as np

def read(input):
    with open(input, 'r') as f:
        return f.read().splitlines()

def checkbingo(entries, checking):
    winners = []
    for entry in bingoinput:
        for p in bingopanels:

            for r in bingopanels[p]:
                if set(r) <= set(checking):
                    if p not in winners:
                        winners.append(p)
                    if len(winners) == len(bingopanels):
                        print("last bingo")
                        return p, r, checking
        
            for r in list(np.array(bingopanels[p]).transpose()):
                if set(r) <= set(checking):
                    if p not in winners:
                        winners.append(p)
                    if len(winners) == len(bingopanels):
                        print("last bingo")
                        return p, r, checking                  
        checking.append(entry)

bingoinput = []
bingopanels = {}
bingo = []
pc = 0
for i, inp in enumerate(read('input.txt')):
    if i == 0:
        bingoinput = [int(z) for z in inp.split(',')]
    elif inp == "" and i != 1:
        bingopanels[pc] = bingo
        bingo = []
        pc += 1
    elif i != 1:
        print(inp)
        bingo.append([int(z) for z in inp.split()])
bingopanels[pc] = bingo

#print(bingoinput) 
#print(bingopanels) 

p, r, checking = checkbingo(bingoinput, bingoinput[:5])
print(p, r, checking)

unmarked = []
for row in bingopanels[p]:
    for elem in row:
        if elem not in checking:
            unmarked.append(elem)

print(unmarked)
print(sum(unmarked))
a = checking[-1] * sum(unmarked)
print(a)




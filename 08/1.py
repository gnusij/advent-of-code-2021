import numpy as np


correct = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg",
}

def read(file):
    with open(file,'r') as f:
        return f.read()

#print(read('sample'))

inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab "

con = inp.split()
lens = [len(i) for i in con]
mapped = {
    "1": [str(i) for i in con[lens.index(2)]],
    "7": [str(i) for i in con[lens.index(3)]],
    "4": [str(i) for i in con[lens.index(4)]],
    "8": [str(i) for i in con[lens.index(7)]],
}

out = "cdfeb fcadb cdfeb cdbaf"


outs = []
for s in read('input').splitlines():
    outs.append(s.split(r'|')[1])
print(outs)
lens = [[len(i) for i in s.split()] for s in outs]
#lens = [[len(i) for i in s.split()] for s in outs]
count=0
for len in lens:
    for i in len:
        if i==2 or i==3 or i==4 or i==7:
            count += 1

print(count)


def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def insert(rules, pt):
    new_pt = str(pt)
    for i in range(len(pt), 1, -1):
        seq = str(pt[i-2:i])
        if seq in rules:
            #print(new_pt[:i+1])
            #print(rules[seq])
            #print(new_pt[i+1:])

            new_pt = new_pt[:i-1] + rules[seq] + new_pt[i-1:]
            #print(new_pt)
    return new_pt

dat = read('sample')
rules = {}
pt = dat[0]
pis = dat[2:]

for pi in pis:
    check = pi.split('->')[0].strip()
    inst = pi.split('->')[1].strip()
    rules[check] = inst

#print(pt)
#print(rules)

step = 10

for i in range(step):
    if i < 5:
        print(i, len(pt), pt)
    else:
        print(i, len(pt))
    pt = insert(rules, pt)

from collections import Counter

res = Counter(pt)
maxs = str(max(res, key = res.get))
mins = str(min(res, key = res.get))

print(maxs, mins)
print(pt.count(maxs) - pt.count(mins))
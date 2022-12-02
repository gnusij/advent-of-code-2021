def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def intersect(l1, l2):
    return list(set(l1) & set(l2))

def dist(p1, p2):
    return round(pow(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2) + pow(p2[2] - p1[2], 2), 0.5),4)

def getk(d, v):
    for i in d.items():
        if i[1] == v:
            return i[0]

s = {} 
c = 0
i = -1
for row in read('sample2'):
    if row.startswith("---"):
        c = 0 
        i += 1
    elif row != "":
        if i not in s.keys(): s[i] = []
        s[i].append(eval(row))
    else:
        c += 1 

print("Sensors")
print(s)

M = {}
for i in s:
    M[i] = {}

for n in range(len(s)):
    for i in range(len(s[n])):
        #if i not in m[n].keys():
        #    m[n][i] = []
        for j in range(i+1, len(s[n])):
            if i != j:
                #m[n][i].append(dist(s[n][i], s[n][j]))
                M[n][(i,j)] = dist(s[n][i], s[n][j])

print("Beacon Dist")
print(M)
        
d = {}
for n in range(len(s)):
    if n not in d.keys():
        d[n] = []
    for j in M[n]:
        d[n].append(M[n][j])
    d[n] = list(set(d[n]))



MM = []

for n in range(len(s)):
    for m in range(n+1, len(s)):
        if n != m:
            inters = intersect(d[n], d[m])
            if len(inters) >= 12:
                print(f"Sensors {n} and {m} overlap: {len(inters)}")
                for inter in inters:
                    kn = getk(M[n], inter)
                    km = getk(M[m], inter)
                    #print(kn, km)
                    if kn != km:
                        for i in range(1):
                            mystr = f"S{n}B{kn[i]} == S{m}B{km[i]}"
                            if mystr not in MM:
                                MM.append(mystr)
print(MM)

print(len(MM))
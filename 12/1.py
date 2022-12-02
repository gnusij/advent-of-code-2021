def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()
    
d = [j.split('-') for j in read('input')]

data = d + [dat[::-1] for dat in d]

for i, dat in enumerate(data):
    if dat[1] == "start":
        data[i] = [dat[1], dat[0]]
    elif dat[0] == "end":
        data[i] = [dat[1], dat[0]]
#print(data)

routes = [i for i in data if i[0] == 'start']

#print(routes)

r = []
allroutes = []

for route in routes:
    visited = [route]
    
    #while True: 
    for i in range(200):

        for r in visited:

            for dat in data:
                #print("for ", r)
                #print("checking ", dat)

                if dat[0] == r[-1] and list(r) + list(dat[1:]) not in visited:
                    if (dat[1].isupper() and r.count(dat[1]) < 3) or\
                       (dat[1].islower() and dat[1] not in r):

                        r = list(r) + list(dat[1:])

                        visited.append(r)

                        #print(visited)

                        if r[-1] == "end" and r not in allroutes:
                            allroutes.append(r)
                            r = []
                            break
    
        
print(len(allroutes))
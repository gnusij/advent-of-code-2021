import numpy as np
from queue import PriorityQueue
from collections import deque, defaultdict

def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def getcell(dat, i, j):
    try:
        return dat[i][j]
    except:
        return None

def add_edge(G, c, dat, i, j):
    if getcell(dat, i, j) and i>=0 and j>=0:
        G[c].append(i*len(dat[0])+j)
    return G


def dijkstra(G, k, start_vertex):
    D = {v:float('inf') for v in range(len(k))}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():

        (dist, current_vertex) = pq.get()

        for neighbor in G[current_vertex]:
            #print("A", neighbor, current_vertex)
            distance = k[neighbor]

            old_cost = D[neighbor]
            new_cost = D[current_vertex] + distance

            if new_cost < old_cost:
                pq.put((new_cost, neighbor))
                D[neighbor] = new_cost
    return D

#dat = [[8]]
dat = [[int(j) for j in i] for i in read('input')]

hlen = len(dat[0])
vlen = len(dat)

d = np.array(dat)

d_tmp = np.array(list(dat))
new_d = np.array(list(dat))


for i in range(4):
    d_tmp = d_tmp + 1
    d_tmp[d_tmp>9] = 1
    new_d = np.concatenate((new_d, d_tmp), axis=1)

d_tmp = np.array(list(new_d))

for i in range(4):
    d_tmp = d_tmp + 1
    d_tmp[d_tmp>9] = 1
    new_d = np.concatenate((new_d, d_tmp), axis=0)

dat = list(new_d)
rowlen = len(dat) 
collen = len(dat[0])

k = {}

G = defaultdict(list)
ii = 0 
for i, row in enumerate(dat):
    for j, dist in enumerate(row):
        k[ii] = dist

        G = add_edge(G, ii, dat, i-1, j)
        G = add_edge(G, ii, dat, i+1, j)
        G = add_edge(G, ii, dat, i, j-1)
        G = add_edge(G, ii, dat, i, j+1)

        ii += 1



dists = dijkstra(G, k, 0)

print(dists[rowlen*collen-1])
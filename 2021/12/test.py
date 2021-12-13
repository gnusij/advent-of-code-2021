from collections import defaultdict

def read(file):
    starts = []
    links = []
    with open(file, 'r') as f:
        d = [j.split('-') for j in f.read().splitlines()]

        data = d + [dat[::-1] for dat in d]

        for i, dat in enumerate(data):
            if dat[1] == "start":
                data[i] = [dat[1], dat[0]]

            elif dat[0] == "end":
                data[i] = [dat[1], dat[0]]

        starts = [i for i in data if i[0] == 'start']
        links = [i for i in data if[0] != 'start']
        return starts, links


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add(self, edge):
        u = edge[0]
        v = edge[1]
        self.graph[u].append(v)

    def allpath(self, u, d, path, visited, allroutes):
        path = path + [u]
        if path not in visited:
            visited.append(path)

        if u == d: 
            return [path], visited
        
        if u not in self.graph:
            return [], visited

        paths = []
        for i in self.graph[u]:
            if (i.islower() and i not in path):
                expath, visited = self.allpath(i, d, path, visited, allroutes)
                for p in expath:
                    paths.append(p)
        return paths, visited



def read2(file):
    with open(file, 'r') as f:
        d = [j.split('-') for j in f.read().splitlines()]
        data = [i[::-1] for i in d] + d 
        return data

g = Graph()
data = read2('input')
for edge in data:
    g.add(edge)

l= g.allpath('start','end', [], [], [])
print(len(l))
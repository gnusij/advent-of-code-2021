def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

class snum:
    def __init__(self, n = '[[[[[9,8],1],2],3],4]'):
        self.n = n
        self.l = eval(self.n)

    def __str__(self):
        return repr(self.l)

    def __add__(self, other):
        return snum(repr([self.l, other.l]))

    def reduce():
        pass

def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0

def getcell(l, i=None, j=None , k=None , u=None):
    if 

#print(snum('[[[[[9,8],1],2],3],4]'))

l = [[[[[9,8],1],2],3],4]

for i in range(len(l)):
    if isinstance(l[i], list): 
        for j in range(len(l[i])):
            if isinstance(l[i][j], list):
                for k in range(len(l[i][j])):
                    if isinstance(l[i][j][k], list):
                        for u in range(len(l[i][j][k])):
                            if isinstance(l[i][j][k][u], list):
                                print("DEPTH 4", l[i][j][k][u])


#   p = None
#   for sn in read('sample'):
#       if p == None:
#           p = snum(sn)
#       else:
#           p = p + snum(sn)
#   print(p)




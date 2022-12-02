import numpy as np

def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()



def gf(seqs):
    n = 0

    def flash(i, j):
        def getcell(i, j):
            try:
                return seqs[i][j]
            except:
                return None
        def inc(i, j):
            if not cell or (i, j) in flashed or i<0 or j<0 or i>9 or j>9:
                return
            seqs[i][j] += 1
            if seqs[i][j] > 9 and (i,j) not in flashed:
                flash(i, j)

        cell = getcell(i, j)
        if not cell or (i, j) in flashed or i<0 or j<0 or i>9 or j>9:
            return
        #
        #    
        #    if first:
        flashed.append((i,j))
        #print(f"flashing {i} {j}")
            
        inc(i-1, j-1) #False)
        inc(i,   j-1) #False)
        inc(i+1, j-1) #False)
        inc(i-1, j, ) #False)
        inc(i+1, j, ) #False)
        inc(i-1, j+1) #False)
        inc(i,   j+1) #False)
        inc(i+1, j+1) #False)


    c = 0
    while True:

        for i,seq in enumerate(seqs):
            for j, o in enumerate(seq):
                seqs[i][j] += 1
            
        flashed = []
        for i,seq in enumerate(seqs):
            for j, o in enumerate(seq):
                if seqs[i][j] > 9 and (i, j) not in flashed:
                    flash(i, j)

        for i,seq in enumerate(seqs):
            for j, o in enumerate(seq):
                if seqs[i][j] > 9:
                    seqs[i][j] = 0
                    n += 1

        l = [i for j in seqs for i in j]
        if len([i for i in l if i == 0]) == len(l):
            print(c+1)
            break
        c += 1

seqs = [[int(j) for j in i] for i in read('input')]
gf(seqs)
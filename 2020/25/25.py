cpk = 5764801
dpk = 17807724

def tr(num, loopsize):
    r = 1
    for i in range(loopsize):
        r = r*num
        r = r%20201227
    return r

sub = 7
cls = 8
dls = 11

tr(sub,cls)
tr(sub,dls)

tr( tr( tr(sub,dls), cls), dls)


value = 1 
loop_size = 0
cpk = 11404017
dpk = 13768789
while value != (cpk):
    value = value * 7 % 20201227
    loop_size += 1

print(pow(dpk, loop_size, 20201227))
pyint = int
def int(x, y = 10):
    return pyint("".join(x), y)

with open('input', 'r') as f: 
    d = f.read().strip()

def read_packet(c):
    ver = int(c[0:3], 2)
    id  = int(c[3:6], 2)
    c[:] = c[6:]

    #print("PV: ", ver)
    #print("ID: ", id)

    # literal
    if id == 4:
        data = []
        while True: 
            t = c.pop(0)
            data += c[:4]
            c[:] = c[4:]
            if t == '0': break
        return (ver, id, int(data,2))
    # operator
    else:
        packets = []

        if c.pop(0) == "0":
            l = int(c[:15],2)
            c[:] = c[15:]
            d = c[:l]
            c[:] = c[l:]
            while d:
                packets.append(read_packet(d))

        else:
            n = int(c[:11],2)
            c[:] = c[11:]
            for _ in range(n):
                packets.append(read_packet(c))

        return (ver, id, packets)

def getval(p):
    id = p[1]
    if id == 0:
        return sum(map(getval, p[2]))
    elif id == 1:
        v = 1
        for pack in p[2]:
            v *= getval(pack)
        return v
    elif id == 2:
        return min(map(getval, p[2]))
    elif id == 3:
        return max(map(getval, p[2]))
    elif id == 4:
        return p[2]
    elif id == 5:
        return 1 if getval(p[2][0]) > getval(p[2][1]) else 0
    elif id == 6:
        return 1 if getval(p[2][0]) < getval(p[2][1]) else 0
    elif id == 7:
        return 1 if getval(p[2][0]) == getval(p[2][1]) else 0

#d = 'C200B40A82'
#d = '9C0141080250320F1802104A08'
#d = '9C005AC2F8F0'
#d = 'CE00C43D881120'

b = list("".join(bin(int(d, 16))[2:].zfill(4) for d in d.strip()))
p = read_packet(b)
print(p)

print(getval(p))

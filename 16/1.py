pyint = int
def int(x, y = 10):
    return pyint("".join(x), y)

with open('input', 'r') as f: 
    d = f.read().strip()

def read_packet(c):
    ver = int(c[0:3], 2)
    id  = int(c[3:6], 2)
    c[:] = c[6:]

    print("PV: ", ver)
    print("ID: ", id)

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
                print(d)
                packets.append(read_packet(d))

        else:
            n = int(c[:11],2)
            c[:] = c[11:]
            for _ in range(n):
                packets.append(read_packet(c))

        return (ver, id, packets)

def sum_vers(p):
    v = p[0]
    id = p[1]
    if id == 4:
        return v 
    else:
        return v + sum(map(sum_vers, p[2]))

    
b = list("".join(bin(int(d, 16))[2:].zfill(4) for d in d.strip()))
p = read_packet(b)
print(sum_vers(p))
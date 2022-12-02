
def step(x, y, vx, vy):
    x += vx
    y += vy
    if vx != 0:
        if vx > 0:
            vx -= 1
        else:
            vx += 1
    vy -= 1 
    return x, y, vx, vy

maxy = float('-inf')

for vxx in range(-500, 123):
    for vyy in range(-500, 123):
        x = 0
        y = 0
        vx = vxx
        vy = vyy

        n = 0
        tmp_maxy = float('-inf')
        while n<100:
            x, y, vx, vy = step(x, y, vx, vy)
            if y > tmp_maxy:
                tmp_maxy = y
            if 124 <= x and x <= 174 and -123 <= y and y <= -86:
            #if 20 <= x and x <= 30 and -10 <= y and y <= -5:
                if tmp_maxy > maxy:
                    maxy = tmp_maxy
                break
            n += 1
print(maxy)

minx = 124
maxx = 174
miny = -123
maxy = -86

def steps_for_dy(dy):
    y = 0
    steps = 0
    valid = []
    while y >= miny:
        if miny <= y <= maxy:
            valid.append(steps)
        y += dy
        dy -= 1
        steps += 1
    return valid

def can_land_dx(step):
    for dx in range(1, maxx):
        x = 0
        for _ in range(step):
            x += dx
            if dx > 0:
                dx -= 1
        if minx <= x <= maxx:
            return True
    return False

dy = -miny

while True:
    if any(can_land_dx(step) for step in steps_for_dy(dy)):
        print(sum(range(1, dy + 1)))
        break
    dy -= 1
import numpy as np

def read(file):
    with open(file,'r') as f:
        return f.read().splitlines()
    
sum = 0

for line in read('input'):
    print(line)
    inp = line.split(r'|')[0]
    out = line.split(r'|')[1]


    con = inp.split()
    lens = [len(i) for i in con]
    mapped = {
        "1": [str(i) for i in con[lens.index(2)]],
        "7": [str(i) for i in con[lens.index(3)]],
        "4": [str(i) for i in con[lens.index(4)]],
        "8": [str(i) for i in con[lens.index(7)]],
    }
    top = list(set(mapped["7"]) - set(mapped["1"]))
    s = [[str(i) for i in j] for j in con]
    leftovers = []
    for nums in s:
        if nums in [m for m in mapped.values()]:
            pass
        else:
            leftovers.append(nums)

    botleftcornor = list(set(mapped["8"]) - set(mapped["4"]) - set(top))
    for i,lo in enumerate(leftovers):
        if len(lo) == 6:
            if not set(botleftcornor).issubset(set(lo)):
                mapped["9"] = lo
                del leftovers[i]
                break

    botleft = list(set(mapped["8"]) - set(mapped["9"]))
    bot = list(set(botleftcornor) - set(botleft))

    for i,lo in enumerate(leftovers):
        if len(lo) == 6:
            if not set(mapped["1"]).issubset(set(lo)): 
                mapped["6"] = lo
                topright = list(set(mapped["8"]) - set(mapped["6"]))
                del leftovers[i]
                break

    for i,lo in enumerate(leftovers):
        if len(lo) == 6:
            mapped["0"] = lo
            del leftovers[i]
            break

    for i,lo in enumerate(leftovers):
        if len(lo) == 5:
            if not set(topright).issubset(set(lo)) and not set(botleft).issubset(set(lo)): 
                mapped["5"] = lo
                del leftovers[i]
                break
    for i,lo in enumerate(leftovers):
        if len(lo) == 5:
            if not set(botleft).issubset(set(lo)): 
                mapped["3"] = lo
                del leftovers[i]
                break

    mapped["2"] = leftovers[0]

    print(mapped)

    digit = ''
    nums = [[str(i) for i in s] for s in out.split()]
    for num in nums:
        for k,v in mapped.items():
            if set(num) == set(v):
                digit += str(k)
    print(digit)
    sum += int(digit)
print(sum)
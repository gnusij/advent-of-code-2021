
import collections
import numpy as np

def read(input):
    with open(input, 'r') as f:
        return f.read().splitlines()

def part1(input):
    block = []
    for inp in read(input):
        block.append([int(i) for i in inp])
    arr = np.array(block)
    arr = arr.transpose()
    seq = ''
    for e in arr:
        seq += str(collections.Counter(e).most_common()[0][0])
    gamma =  int(seq,2)
    eps = int(seq.replace('0','2').replace('1','0').replace('2','1'),2)
    return gamma*eps

def part2(input):
    block = []
    for inp in read(input):
        block.append([int(i) for i in inp])
    arr = np.array(block)
    i = 0
    while True:
        arr = get_oxy(i, arr)
        if len(arr) == 1:
            break
        i += 1
    oxy = int(''.join([str(i) for i in arr[0]]),2)

    arr = np.array(block)
    i = 0
    while True:
        arr = get_co2(i, arr)
        if len(arr) == 1:
            break
        i += 1
    co2 = int(''.join([str(i) for i in arr[0]]),2)

    return oxy*co2

def get_oxy(i, arr):
    bit = arr.transpose()[i]
    max_len = len(arr.transpose()[0])
    most_common, most_freq = get_most_common(bit)

    if len(arr) == 1:
        return arr
    keep = []
    crt = most_common
    for rowbit in arr:
        if max_len/2 == most_freq:
            crt = 1
        
        if int(rowbit[i]) == crt:
            keep.append(list(rowbit))
    return np.array(keep)


def get_co2(i, arr):
    bit = arr.transpose()[i]
    max_len = len(arr.transpose()[0])
    least_common, least_freq = get_least_common(bit)

    if len(arr) == 1:
        return arr
    keep = []
    crt = least_common
    for rowbit in arr:
        if max_len/2 == least_freq:
            crt = 0
        
        if int(rowbit[i]) == crt:
            keep.append(list(rowbit))
    return np.array(keep)



def get_most_common(bit):
    com = collections.Counter(bit).most_common()[0]
    most_common = com[0]
    freq = com[1] 
    return most_common, freq

def get_least_common(bit):
    com = collections.Counter(bit).most_common()[-1]
    least_common = com[0]
    freq = com[1] 
    return least_common, freq


def main():
    puzzle = {
        '1':part1,
        '2':part2,
    }
    for i in ['1', '2']:
        print("="*100 + f"\nPART{i}:")
        print(f"SAMPLE ANSWER: {puzzle[i]('sample.txt')} ")
        print(f"INPUT  ANSWER: {puzzle[i]('input.txt')} ")

if __name__ == "__main__":
    main()
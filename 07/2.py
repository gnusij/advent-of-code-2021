import numpy as np

def read(file):
    with open(file, 'r') as f:
        return [int(i) for i in f.read().split(',')]

nums = np.array(read('sample'))
sums = []
for c in range(min(nums), max(nums)):
    sum = 0
    for i in nums:
        n = abs(c - i)
        sum += n*(n+1)/2
    sums.append(sum)

print(min(sums))

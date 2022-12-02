import numpy as np
import matplotlib.pyplot as plt

def read(file):
    with open(file, 'r') as f:
        return [int(i) for i in f.read().split(',')]

nums = read('input')

print(np.round(np.mean(nums)))

sums = []
index = [] 
for c in range(min(nums), max(nums)):
    sum = 0
    for i in nums:
        n = abs(c - i)
        sum += n*(n+1)/2
    sums.append(sum)
    index.append(c)

print(index[sums.index(min(sums))])

plt.figure()
plt.plot(index, sums)
plt.scatter(index[sums.index(min(sums))], min(sums))
plt.show()

import numpy as np

def read(file):
    with open(file, 'r') as f:
        return [int(i) for i in f.read().split(',')]

nums = np.array(read('input'))

center = np.median(nums)
print(sum(abs(nums - center)))
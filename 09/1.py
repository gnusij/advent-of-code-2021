import numpy as np
import itertools as it

def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

nums = [[int(i) for i in row] for row in read('input')]
print(nums)

lows= []
for i in range(len(nums)):
    for j in range(len(nums[i])):
        #print(f"checking {i},{j}    num:{nums[i][j]}")
        # topleft
        if j == 0 and i == 0:
            if nums[i][j] < nums[i][j+1] and nums[i][j] < nums[i+1][j]:
                lows.append(nums[i][j])
        # topright
        elif j == len(nums[i])-1 and i == 0:
            if nums[i][j] < nums[i][j-1] and nums[i][j] < nums[i+1][j]:
                lows.append(nums[i][j])
        # botleft
        elif j == 0 and i == len(nums)-1:
            if nums[i][j] < nums[i][j+1] and nums[i][j] < nums[i-1][j]:
                lows.append(nums[i][j])
        # botright
        elif j == len(nums)-1 and i == len(nums)-1:
            if nums[i][j] < nums[i][j-1] and nums[i][j] < nums[i-1][j]:
                lows.append(nums[i][j])
        # top
        elif i == 0 and (j != 0 and j !=len(nums[i])-1):
            if nums[i][j] < nums[i][j+1] and nums[i][j] < nums[i][j-1] and nums[i][j] < nums[i+1][j]:
                lows.append(nums[i][j])
        # bottom
        elif i == len(nums)-1 and (j != 0 and j !=len(nums[i])-1):
            if nums[i][j] < nums[i][j+1] and nums[i][j] < nums[i][j-1] and nums[i][j] < nums[i-1][j]:
                lows.append(nums[i][j])
        # left
        elif j == 0:
            if nums[i][j] < nums[i][j+1] and nums[i][j] < nums[i+1][j] and nums[i][j] < nums[i-1][j]:
                lows.append(nums[i][j])
        # right
        elif j == len(nums[i])-1:
            if nums[i][j] < nums[i][j-1] and nums[i][j] < nums[i+1][j] and nums[i][j] < nums[i-1][j]:
                lows.append(nums[i][j])
        else:
            if nums[i][j] < nums[i][j-1] and nums[i][j] < nums[i][j+1] and nums[i][j] < nums[i-1][j] and nums[i][j] < nums[i+1][j]:
                lows.append(nums[i][j])
print(sum([int(i)+1 for i in lows])) 



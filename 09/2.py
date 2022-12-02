def read(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def getCell(nums, i, j):
    try:
        return nums[i][j]
    except:
        return None

def walk(nums, i, j, start, groups, group, visited):
    cell = getCell(nums, i, j)

    if cell == None or cell == 9 or (i,j) in visited or i<0 or j<0:
        return groups, group, visited

    #print(f"checking {cell}, {i}, {j}")
    group.append(cell)
    visited.append((i,j))
    groups, group, visited = walk(nums, i + 1, j, False, groups, group, visited)
    groups, group, visited = walk(nums, i - 1, j, False, groups, group, visited)
    groups, group, visited = walk(nums, i, j+1, False, groups, group, visited)
    groups, group, visited = walk(nums, i, j-1, False, groups, group, visited)
    if start:
        groups.append(group)
        group = []
    return groups, group, visited

def getgroups(nums):
    visited = []
    groups = []
    group = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            groups, group, visited = walk(nums, i, j, True, groups, group, visited)
    return groups

nums = [[int(i) for i in row] for row in read('input')]
groups = getgroups(nums)
s = 1
l = [len(group) for group in groups]

for i in sorted(l, reverse=True)[:3]:
    s *= i
print(s)
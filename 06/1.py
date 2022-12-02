
def read(file):
    with open(file, 'r') as f: return f.read().splitlines()

def dup(nums):
    new_nums = nums[:]
    for i, num in enumerate(nums):
        if num == 0:
            new_nums[i] = 6 
            new_nums.append(6 + new)
        else:
            new_nums[i] -= 1
    return new_nums

new = 2

nums = [ int(i) for i in read('i')[0].split(',')]

day = 0
while day != 80:
    nums = dup(nums)
    day += 1

print(len(nums))
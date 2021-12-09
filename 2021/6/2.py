def read(file):
    with open(file, 'r') as f: return f.read().splitlines()

nums = [int(i) for i in read('i')[0].split(',')]
print(nums)

nums = [nums.count(i) for i in range(7+2)]
print(nums)

for i in range(256): 
    nums.append(nums.pop(0))
    nums[6] += nums[8]
print(sum(nums))


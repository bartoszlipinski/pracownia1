nums = [-15,8,-31,47,-2,19]

min = nums[0]
max = nums[0]

for num in nums:
    if num > max:
        max = num
    if num < min:
        min = num
        
print(f'Min = {min}, max = {max}')
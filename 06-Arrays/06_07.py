nums = [1,2,5,7,14,20,49,66,99]
even = 0
odd = 0
for i in nums:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
        
print(f'Odd nums: {odd}, Even nums: {even}')
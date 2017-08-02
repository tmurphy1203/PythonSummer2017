nums = range(1, 10)
twice = []

for n in nums:
    if n > 4:
        twice.append(n * 2)
    
twice = [n * 2 for n in nums if n > 4]   
    
print nums
print twice

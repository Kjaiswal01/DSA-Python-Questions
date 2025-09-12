#  Lower-Bound -------------------------------------------------

nums = [1,1,1,3,3,3,5,6,7,7,7,9,9,12,12,12,13]
n = len(nums)
target = 7  
lb = n
low = 0
high = n-1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid 
        high = mid -1
    else:
        low = mid + 1  
print(lb) #-->8    

#  upper Bound -------------------------------------------------
nums = [1,1,1,3,3,3,5,6,7,7,7,9,9,12,12,12,13]
n = len(nums)
target = 9
ub = n
low = 0
high = n-1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] > target:
        ub = mid 
        high = mid -1
    else:
        low = mid + 1  
print(ub)   #---> 13   



# Leet code 35 - SEARCH INSERT POSITION ---------Same code as their lower bound -----------------
nums = [1,1,1,3,3,3,5,6,7,7,7,9,9,12,12,12,13]
n = len(nums)
target = 2
lb = n
low = 0
high = n-1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid 
        high = mid -1
    else:
        low = mid + 1  
print(lb) #--> 3
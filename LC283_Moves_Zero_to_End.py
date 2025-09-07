# Leet Code 283
# ---- Method 1 — Using a temporary list (Extra Space) (Brute Method)

nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
temp  = []                            # ① temporary list to hold non-zero elements

# First pass – collect all non-zero elements
for i in range(n):
    if nums[i] != 0:                  # if element is non-zero
        temp.append(nums[i])          # add to temp

    
nz = len(temp)                        # ③ count of non-zero elements

# Put non-zero elements back to the original array
for i in range(nz):
    nums[i] = temp[i]                 # overwrite from start with non-zeros

# Fill remaining part with zeros
for i in range(nz, n):
    nums[i] = 0                       # fill zeros at the end
print(nums)

# How to remember:
# “Collect non-zeros”
# “Write them back”
# “Fill zeros at end”

# TC: O(n) --------------
# 3 loops but total still proportional to n.

# SC: O(n) ---------------
# Extra list temp may be as large as original array.


# ----------------------------------------------------------------------------------------------


# -----Method 2 — Two-pointer in-place swap (Optimal)
nums = [1,2,4,0,3,0,0,3,5,1,0,8,0,9,1]
n = len(nums)

def Z_E(nums):
    if len(nums) == 1:                 # edge case: single element
        return

    # Find index i of first zero
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break                      # stop at first zero
        i += 1
    if i == len(nums):                 # no zeros found
        return nums                    # already all non-zero

    # j starts after i, scanning ahead
    j = i + 1
    while j < len(nums):               # until end of array
        if nums[j] != 0:               # if current element is non-zero
            nums[i], nums[j] = nums[j], nums[i]  # swap with zero at i
            i += 1                     # move i to next zero position
        j += 1                         # always move j ahead

    return nums

print(Z_E(nums))

# How to remember :
# i marks where the next non-zero should go
# j scans for the next non-zero
# When found, swap and move i
# This is exactly like “partitioning” the array.

# TC: O(n)
# Both i and j traverse the list once.

# SC: O(1)
# No extra array, just two indices
    


# -----------Looping Method--------------- -------------------------
# Time Complexity (TC): O(n) (one pass)
# Space Complexity (SC): O(1) (in-place)

nums = [5, -2, 3, 9, 0, 6, 10, 7]

n = len(nums)
temp = nums[n-1]             # store last element
for i in range(n-2, -1, -1): # shift elements from end towards right
    nums[i+1] = nums[i]
nums[0] = temp               # put last element at first position
print(nums)  # Output: [7, 5, -2, 3, 9, 0, 6, 10]
  

# -------Slicing method------------------------------------------------------
# Time Complexity (TC): O(n) (creates a new list and copies)
# Space Complexity (SC): O(n) (because slicing creates a temporary list)

nums = [5, -2, 3, 9, 0, 6, 10, 7]

# rotate right by one using slicing
nums[:] = nums[-1:] + nums[:-1]   # last element + rest of list
print(nums)  # Output: [7, 5, -2, 3, 9, 0, 6, 10]



#----------------- Loop + Pop/Insert method------------------------------
nums = [3,9,5,6,7,2]       # original list

n = len(nums)              # total elements
k = 2                      # rotate right by k positions
rotations = k % n          # in case k > n

for i in range(rotations): # repeat k times
    e = nums.pop()         # take the last element out
    nums.insert(0,e)       # insert it at the beginning

print(nums)  # [7,2,3,9,5,6]

# ------------Time Complexity (TC):--------------
# pop() from end → O(1)
# insert(0, e) at front → O(n) (because shifting all elements)
# Doing this k times → O(k·n) worst case.

# -------------Space Complexity (SC):-------------
# No extra big array used → O(1) (in-place)

# ------------------------------------------------------------------------------------------------

# -------------------Slicing + Concatenation method---------------------------
nums = [3,9,5,6,7,2]     # original list

n = len(nums)
k = 3                    # rotate right by k
k = k % n                # handle k > n

# take last k elements + first n-k elements
nums[:] = nums[n-k:] + nums[:n-k]

print(nums)  # [6,7,2,3,9,5]


# -------------Time Complexity (TC):---------------
# Slicing both parts + concatenating → O(n) (creates a new combined list of size n once).

# --------------Space Complexity (SC):-----------------
# Because slices create new lists temporarily → O(n) extra space (not purely in-place)


# ------------------------------------------------------------------------
# --------------Reversal Algorithm for Array Rotation---------------------- 
nums = [3,9,5,6,7,2,10,9]
n = len(nums)
k = 3                   # rotate right by 3 steps

def reverse(nums, left, right):
    while left < right :
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Step 1: reverse entire array
reverse(nums, 0, n-1)

# Step 2: reverse first k elements
reverse(nums, 0, k-1)

# Step 3: reverse remaining n-k elements
reverse(nums, k, n-1)

print(nums)


# Initial array: [3,9,5,6,7,2,10,9]

# Step 1 (reverse whole array) → [9,10,2,7,6,5,9,3]
# Step 2 (reverse first k=3) → [2,10,9,7,6,5,9,3]
# Step 3 (reverse remaining n-k=5) → [2,10,9,3,9,5,6,7]
# This is now the array rotated to the right by 3 positions.


# Time Complexity (TC)-------------------
# reverse(nums, 0, n-1) → O(n)
# reverse(nums, 0, k-1) → O(k)
# reverse(nums, k, n-1) → O(n-k)
# Total = O(n + k + n-k) = O(n)

# Space Complexity (SC)------------------
# Only constant extra variables (left, right, and temp for swap)
# So O(1) extra space.
# ---------------Method 1: Brute Force (check every pair)----------------
nums = [5,9,1,2,4,15,6,3]  # list of numbers
target = 13                # sum we want
n = len(nums)              # length of list

# Check every possible pair of indices (i,j)
for i in range(n-1):                 # first index goes from 0 to n-2
    for j in range(i+1, n):           # second index goes from i+1 to n-1
        if nums[i] + nums[j] == target:  # check if the pair sums to target
            print(f"Indexes {i} and {j} sum to target {target}") 
            # print(i,j)
            # print their indices


# Time Complexity (TC): O(n²) because of nested loops (every pair is checked)
# Space Complexity (SC): O(1) because we’re not using any extra space



# --------------Method 2: Hash Map (fast way)---------------------------------------------
nums = [5,9,1,2,4,15,6,3]  # list of numbers
target = 13                # sum we want
n = len(nums)              # length of list

hash_map = {}  # dictionary to store: number -> its index

for i in range(n):   
    remaining = target - nums[i]    # find what number we need to complete target
    if remaining in hash_map:       # check if we’ve already seen that needed number
        print(f"Indexes {hash_map[remaining]} and {i} sum to target {target}")
        # print the stored index of needed number and current index
    hash_map[nums[i]] = i           # store current number with its index for future checks


# TC: O(n) because we’re doing just one pass through the list (dictionary lookup is O(1) average).
# SC: O(n) because hash_map may store all elements.
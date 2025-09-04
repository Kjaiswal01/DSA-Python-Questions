# ------- Method 1: Using for loop & flag ---------------------------
nums = [3, 5, 6, 8, 9, 10, 30]   # our list
n = len(nums)                    # total elements
is_sorted = True                 # assume initially array is sorted

# Loop through indices from 0 to n-2
for i in range(0, n-1):
    # If current element > next element, array is not sorted
    if nums[i] > nums[i+1]:
        is_sorted = False
        break                    # no need to check further, break out
print("Method 1 result:", is_sorted)  # True if sorted, False if not


# ------ Method 2: Compare with sorted() ---------------------------
# sorted(nums) returns a new sorted list. If nums is already sorted,
# it will be exactly equal to sorted(nums).
print("Method 2 result:", nums == sorted(nums))


#----- Method 3: Using all() + generator ---------------------------
# all() returns True if all conditions inside are True.
# Here we check for every i: nums[i] <= nums[i+1]
is_sorted = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
print("Method 3 result:", is_sorted)


# TC - TIME COMPLEXITY 
# Method 1 (loop + flag): TC = O(n), SC = O(1)
# Method 2 (sorted()): TC = O(n log n), SC = O(n)
# Method 3 (all()): TC = O(n), SC = O(1)
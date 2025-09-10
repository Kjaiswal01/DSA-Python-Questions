# method 1-----------Brute-force with 4 nested loops
nums = [1, 0, -1, 5, -2, 2, 0, 9]
target = 0
n = len(nums)

# Step 0: If less than 4 elements, no quadruplet is possible
if n < 4:
    result = []
else:
    my_set = set()  # To store unique quadruplets as tuples (to avoid duplicates)

    # Step 1: Use 4 nested loops to check all possible quadruplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    # Step 2: Check if sum equals target
                    if total == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()  # Sort to avoid duplicate quadruplets like [1,0,-1,0] vs [-1,0,0,1]
                        my_set.add(tuple(temp))  # Add as tuple to set

    # Step 3: Convert set of tuples to list of lists
    result = [list(ans) for ans in my_set]

print(result)

# Time Complexity :------------------------
# Total TC = O(n⁴) → very slow for large arrays

# Space Complexity:-------------------------
# Auxiliary SC = O(1) ignoring output storage

# --------------------------------------------------------------------------------------------------------

# method 2-----Optimized using Hash Set for 2-sum------------------------------
nums = [1, 0, -1, 5, -2, 2, 0, 9]
target = 0
n = len(nums)
my_set = set()  # To store unique quadruplets as tuples

# Step 1: Fix first two elements using outer loops
for i in range(n):
    for j in range(i + 1, n):
        hash_set = set()  # Step 2: Hash set to store seen numbers for 2-sum

        # Step 3: Loop for the third element
        for k in range(j + 1, n):
            # Step 4: Find the 4th number that completes the quadruplet
            fourth = target - (nums[i] + nums[j] + nums[k])

            # Step 5: Check if this 4th number was seen before in this loop
            if fourth in hash_set:
                # Valid quadruplet found
                temp = [nums[i], nums[j], nums[k], fourth]
                temp.sort()  # Sort to avoid duplicates
                my_set.add(tuple(temp))  # Add as tuple to set

            # Step 6: Add current number to hash_set for future 2-sum checks
            hash_set.add(nums[k])

# Step 7: Convert set of tuples to list of lists
result = [list(ans) for ans in my_set]
print(result)

# Time Complexity :------------------------
# Total TC = O(n³) → faster than brute-force O(n⁴)

# Space Complexity:-------------------------
# Auxiliary SC = O(n) + O(1)` (ignoring output storage)

# -----------------------------------------------------------------------------------------------

# method 3----------Optimal 4-Sum using Sorting + Two Pointers--------------------------------------------
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    # n: length of input array
    n = len(nums)
    
    # ans: final list to store all unique quadruplets
    ans = []
    
    # Step 1: sort the array
    # Sorting helps to use two-pointer technique and easily skip duplicates
    nums.sort()  

    # Step 2: fix the first element of quadruplet
    for i in range(n):
        # Skip duplicate first elements to avoid repeated quadruplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Step 3: fix the second element of quadruplet
        for j in range(i + 1, n):
            # Skip duplicate second elements to avoid repeated quadruplets
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Step 4: use two pointers for the remaining two elements
            k = j + 1  # left pointer
            l = n - 1  # right pointer

            # Step 5: move pointers until they meet
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    # Found a valid quadruplet
                    ans.append([nums[i], nums[j], nums[k], nums[l]])

                    # Move both pointers inward
                    k += 1
                    l -= 1

                    # Skip duplicates for the third element
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1

                    # Skip duplicates for the fourth element
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                elif total < target:
                    # Sum too small → move left pointer right to increase sum
                    k += 1
                else:
                    # Sum too large → move right pointer left to decrease sum
                    l -= 1

    # Step 6: return the final list of quadruplets
    return ans

# Example run
print(fourSum([1,1,1,1,2,2,3,3,3,4,4,4,5,5,5], 8))

# Time Complexity (TC):----------------------------
# Sorting array → O(n log n)
# Outer loops i and j → O(n²)
# Two-pointer scan inside → O(n)
# Total TC = O(n³) (optimal for 4-sum problem)

# Space Complexity (SC):------------------------------
# Extra space for pointers → O(1)
# Answer list ans → stores all quadruplets → O(number of quadruplets)
# Auxiliary SC = O(1) (ignoring output storage)
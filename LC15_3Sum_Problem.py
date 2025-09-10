# Aapko ek array diya gaya hai,
# aur aapko aise 3 elements ka combination find karna hai jinka sum 0 ho.


# method 1 ---------(Brute force)------------------------------------------
# Input array
arr = [-1, 0, 1, 2, -1, -4]

# Length of the array
n = len(arr)

# Using a set to store unique triplets (avoids duplicates)
my_set = set()

# Loop 1: pick first element
for i in range(0, n):
    # Loop 2: pick second element after i
    for j in range(i + 1, n):
        # Loop 3: pick third element after j
        for k in range(j + 1, n):
            # Check if sum of three numbers is zero
            if arr[i] + arr[j] + arr[k] == 0:
                # Make a list of the triplet
                temp = [arr[i], arr[j], arr[k]]
                
                # Sort the triplet so that [-1,0,1] and [0,-1,1] are treated as same
                temp.sort()
                
                # Convert to tuple (because set cannot store lists)
                my_set.add(tuple(temp))

# Convert each tuple back to list for final output
print([list(ans) for ans in my_set])

# Possible triplets whose sum = 0:
# (-1, -1, 2)
# (-1, 0, 1)

# Time Complexity (TC):----------------
# Outer loop runs n times.
# Second loop runs up to n times for each i.
# Third loop runs up to n times for each (i, j).
# O(n3)-------
# Sorting the small triplet (temp.sort()) takes O(3 log 3) = O(1) constant time.
# So overall still O(n³).

# Space Complexity (SC):-----------------------
# my_set stores the unique triplets
# In the worst case, it can store all possible triplets → O(n³) in size, but usually far less.
# Temporary list temp → O(1).
# No extra arrays of size n created.
# So SC = O(n³) in worst case due to storage of triplets, but auxiliary SC = O(1).


# -----------------------------------------------------------------------------------------------------------------------------


# method 2 --------(Hashing + Two-sum idea)------- better than brute (n2)
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)

# 'result' set stores unique triplets (converted to tuple for immutability)
result = set()

# Outer loop: fix the first element
for i in range(0, n):
    # 'my_set' will store numbers we have seen for this 'i'
    my_set = set()
    
    # Inner loop: check for pairs that along with arr[i] make sum = 0
    for j in range(i + 1, n):
        # The third number we need to make the sum zero
        third = -(arr[i] + arr[j])
        
        # If 'third' already seen in this iteration, we found a triplet
        if third in my_set:
            temp = [arr[i], arr[j], third]
            temp.sort()  # sort to avoid ordering issues
            result.add(tuple(temp))  # add unique triplet as tuple
        
        # Add the current number to the seen set for this 'i'
        my_set.add(arr[j])

# Convert each tuple back to list for final output
print([list(ans) for ans in result])

# Time Complexity :
# O(n²) — much better than O(n³).

# Space Complexity:
# Auxiliary SC = O(n) per iteration for my_set.
# Total SC = O(n²) worst-case including result storage.



# method 3---(optimal--> two-pointer + sorted array)-----------------------------

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans: final list of unique triplets whose sum = 0
        ans = []
        n = len(nums)

        # Step 1: sort the array to easily skip duplicates
        nums.sort()

        # Step 2: iterate each number as the first element of the triplet
        for i in range(n):
            # skip duplicate first elements to avoid repeating triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: use two pointers for the rest of the array
            j = i + 1            # left pointer just after i
            k = n - 1            # right pointer at the end

            # Step 4: move j and k to find pairs whose sum = -nums[i]
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    # sum too small → move left pointer right to increase sum
                    j += 1
                elif total_sum > 0:
                    # sum too large → move right pointer left to decrease sum
                    k -= 1
                else:
                    # Found a triplet
                    ans.append([nums[i], nums[j], nums[k]])

                    # move both pointers inward
                    j += 1
                    k -= 1

                    # skip duplicate values at j to avoid repeated triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # skip duplicate values at k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        # return the final list of triplets
        return ans

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]


# Time Complexity:----------------------------
# O(n2)+O(nlogn)≈O(n2)

# Space Complexity (SC):---------------------
# O(1) extra space (besides output)
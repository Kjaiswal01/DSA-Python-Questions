#----------------- Brute Method (Two Lists + Rewriting)
# Initial list
nums = [5,10,-3,-1,-10,6]

# Step 1: Separate positives and negatives into two lists
pos = [x for x in nums if x >= 0]   # all positive numbers
neg = [x for x in nums if x < 0]    # all negative numbers

# Step 2: Rearrange nums in place using pos and neg alternately
for i in range(len(pos)):           # we assume len(pos) == len(neg) here
    nums[2*i] = pos[i]              # place positive at even index
    nums[2*i + 1] = neg[i]          # place negative at odd index

print(nums)                         # final rearranged list
# Output:[5, -3, 10, -1, 6, -10]

# Time Complexity :---------------------
# Step 1 (list comprehensions): O(n) + O(n) = O(n)
# Step 2 (loop): O(n/2) = O(n)
# Total = O(n)

# Space Complexity :-------------------------
# Extra space for pos and neg: O(n)
# No additional array except these two lists.
# Total = O(n)


#------------------------------------------------------------------------------------------------------ 


# ----------------------Optimal Method (Single Pass + Direct Placement)
nums = [5,10,-3,-1,-10,6]
n = len(nums)

# Pre-allocate a result array of size n (all zeros initially)
result = [0]*n

# pos_idx starts at 0 for placing positives at even indices
# neg_idx starts at 1 for placing negatives at odd indices
pos_idx ,neg_idx = 0,1

# Single pass over original nums
for i in range(n):
    if nums[i] >= 0:               # if current number is positive
        result[pos_idx] = nums[i]  # place it at current positive index
        pos_idx += 2               # move to next even index
    else:                          # if current number is negative
        result[neg_idx] = nums[i]  # place it at current negative index
        neg_idx += 2               # move to next odd index

print(result)                      # final rearranged list
# Output:[5, -3, 10, -1, 6, -10] 

# Time Complexity :--------------------------
# Only one loop over nums → O(n)

# Space Complexity :---------------------------
# One extra array result of size n → O(n)
# (No need to create two separate lists.)
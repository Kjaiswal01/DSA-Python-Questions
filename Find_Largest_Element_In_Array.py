# --------------------------------------------------------------
# Find First_Largest_Element 
# --------------------------------------------------------------

nums = [55, 33, 66, -88, 88, 95, 2, 99]

def First_Largest_Element(nums):
    largest = nums[0]         # assume first element is largest initially
    n = len(nums)             # length of list
    for i in range(0, n):     # iterate over all elements
        largest = max(largest, nums[i])  # update largest if current > largest
    return largest            # return final largest element

# DRIVER CODE
print("Largest Element is:", First_Largest_Element(nums))

# Time Complexity: O(n) (because we check each element once)
# Space Complexity: O(1) (we use only a few variables)


# --------------------------------------------------------------
# Find Second_Largest_Element (2-pass method)
# --------------------------------------------------------------

nums = [55, 33, 66, -88, 88, 95, 2, 99]

def S_L_E(nums):
    largest = float("-inf")      # initialize largest with -∞
    s_largest = float("-inf")    # initialize second largest with -∞
    n = len(nums)
    
    # Step 1: Find largest element
    for i in range(n):
        largest = max(largest, nums[i])
    
    # Step 2: Find second largest element (excluding the largest)
    for i in range(n):
        if nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    
    return s_largest             # return final second largest

print("Second Largest Element:", S_L_E(nums))

# Time Complexity: O(2n) ≈ O(n) (two separate loops, still linear)
# Space Complexity: O(1)


# --------------------------------------------------------------
# Optimal Method to Find Second_Largest_Element (1-pass method)
# --------------------------------------------------------------

nums = [56, 84, 78, 95, 28, 97, 99]

def S_L_E_2(nums):
    largest = float("-inf")      # initialize largest with -∞
    s_largest = float("-inf")    # initialize second largest with -∞
    n = len(nums)
    
    # Single loop to find largest and second largest simultaneously
    for i in range(n):
        if nums[i] > largest:
            # If current element > largest, shift current largest to second
            s_largest = largest
            largest = nums[i]
        elif nums[i] > s_largest and nums[i] != largest:
            # Else if current > second largest (but not equal to largest)
            s_largest = nums[i]
    return s_largest

print("Second Largest Element (Optimal):", S_L_E_2(nums))

# Time Complexity: O(n) (single pass)
# Space Complexity: O(1)

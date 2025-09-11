# Method 1: Iterative Binary Search--------------------------------------------
# Input sorted array
nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 18

def binary_search(nums, target):
    # Initialize start and end indexes of the search space
    low = 0
    high = len(nums) - 1   # last index
    
    # Loop continues until the search space becomes empty
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2
        
        # Case 1: Target found at mid index
        if nums[mid] == target:
            return mid   # return index
        
        # Case 2: Target is greater than middle element → search in right half
        elif nums[mid] < target:
            low = mid + 1
        
        # Case 3: Target is less than middle element → search in left half
        else:
            high = mid - 1
    
    # If not found after the loop, return -1
    return -1

print(binary_search(nums, target))  # Output: 6

# Time Complexity (TC):---------------------------
# Each step halves the search space.
# So TC = O(log n) where n = len(nums).

# Space Complexity (SC):-------------------------------
# We only use low, high, mid variables.
# So SC = O(1) (constant extra space).



# Method 2: Recursive Binary Search-----------------------------------------------

# Input sorted array
nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 20

def binary_search(nums, low, high, target):
    # Base case: search space empty → target not found
    if low > high:
        return -1
    
    # Calculate middle index
    mid = (low + high) // 2
    
    # Case 1: Target found at mid index
    if nums[mid] == target:
        return mid
    
    # Case 2: Target is greater than mid element → search in right half
    elif nums[mid] < target:
        return binary_search(nums, mid + 1, high, target)
    
    # Case 3: Target is less than mid element → search in left half
    else:
        return binary_search(nums, low, mid - 1, target)

print(binary_search(nums, 0, len(nums) - 1, target))  # Output: -1

# Time Complexity (TC):--------------------------
# Same as iterative: Each call halves the search space.
# TC = O(log n).

# Space Complexity (SC):------------------
# Extra space due to recursive call stack.
# For O(log n) calls, SC = O(log n).
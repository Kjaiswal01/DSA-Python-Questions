# method 1 -------code “works but not clean"---------------------------------------------

# nums = [4,9,8,2,3,1,0,7,6,-2]
# n = len(nums)
# k = 9
# def lin_srch(nums):
#     for i in range(0,n):
#         if nums[i] == k:
#             return i
#     return -1
# print(lin_srch(nums))            



# method 2 --------------------clean version---------------------------------------------
# Function to perform Linear Search
def lin_srch(nums, k):
    """
    Linear Search Function:
    nums : list of elements in which we want to search
    k    : element to find
    Returns index of first occurrence of k if found, else -1
    """
    # iterate over the indices of the list
    for i in range(len(nums)):   
        # check if the current element equals k
        if nums[i] == k:         
            return i             # return the index immediately if found
    return -1                    # if loop ends without finding, return -1

# -----------------Driver code-----------------
nums = [4, 9, 8, 2, 3, 1, 0, 7, 6, 2]  # list of numbers
k = 0                                  # element to search
print(lin_srch(nums, k))               # prints index of first '2'


# Time complexity :------------------------------
# Worst case: we check all n elements once → O(n)
# Best case: element at index 0 → O(1)

# space complexity :--------------------------------
# We use only one loop variable i → O(1) extra space

# Function self-contained hai (bahar ke variables par depend nahi hai).
# len(nums) function ke andar hi call hota hai (no extra n).
# Readable aur maintainable hai.
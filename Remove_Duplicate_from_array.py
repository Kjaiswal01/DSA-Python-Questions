# ----- Brute method -------------------------
# Input array must be sorted for this approach to work
nums = [1,1,1,2,3,4,4,7,9,9,10]

def remove_duplicates_inplace(nums):
    # Edge case: if empty list, nothing to do
    if not nums:
        return 0

    j = 1  # 'j' = index where next unique element will be placed
    # Loop through all elements starting from index 1
    for i in range(1, len(nums)):
        # If current element != previous unique element, it's a new unique number
        if nums[i] != nums[j-1]:
            nums[j] = nums[i]  # place it at 'j'
            j += 1             # increment j to next position
    return j  # j is the count of unique elements

# Driver code
new_len = remove_duplicates_inplace(nums)
print("New length:", new_len)                # number of unique elements
print("After removing dups:", nums[:new_len]) # array up to new_len has unique items


# Time Complexity (TC): O(n) — single pass over the array
# Space Complexity (SC): O(1) — no extra data structures; in-place modification


# --------------------Optimal Swap-Based Two-Pointer (LeetCode style)-------------------------------------------------------------

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # If array has only one element, it's already unique
        if len(nums) == 1:
            return 1

        i = 0          # 'i' = index of last unique element found
        j = i + 1      # 'j' = index scanning through array

        while j < len(nums):
            # If a new unique element is found at j:
            if nums[j] != nums[i]:
                i += 1                       # move i to next position
                nums[j], nums[i] = nums[i], nums[j]  # swap to bring unique at position i
            j += 1   # always move j ahead to check next element

        return i + 1   # length of unique portion = i+1

# Driver code:
nums = [1,1,1,2,3,4,4,7,9,9,10]
sol = Solution()
new_len = sol.removeDuplicates(nums)
print("Length:", new_len)            # count of unique numbers
print("Unique part:", nums[:new_len]) # array up to new_len has unique numbers


# Time Complexity (TC): O(n) — each element inspected once
# Space Complexity (SC): O(1) — does everything in-place, no extra space
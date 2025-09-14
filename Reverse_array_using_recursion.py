# Method 1 – Simple Recursive Reverse for Subarray

def func(arr, left, right):
    if left >= right:       # Base case: stop when pointers cross
        return
    arr[left], arr[right] = arr[right], arr[left]  # Swap elements at left and right
    func(arr, left + 1, right - 1)                # Recursive call for inner subarray

# Example usage
arr = [5,6,9,7,8,3,1,2,55,66,77,88,99]
func(arr, 2, 8)  # Reverse elements from index 2 to 8
print(arr)


# Intuition:
# Imagine you have 2 pointers (left and right) at ends of the subarray.
# Swap elements at these pointers, then move left forward and right backward.
# Stop when left >= right.
# Output:
# [5, 6, 55, 2, 1, 3, 8, 7, 9, 66, 77, 88, 99]

# Time Complexity (TC): O(n) → n = number of elements in the subarray (right - left + 1)
# Space Complexity (SC): O(n) recursion stack



# Method 2 – Using Class & Recursive Function (Full Array)
class Solution:
    def reverseArray(self, arr, left, right):
        # Base case: stop when pointers cross
        if left >= right:
            return
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Recursive call for inner subarray
        self.reverseArray(arr, left + 1, right - 1)

# Driver code
obj = Solution()
arr = [5, 55, 6, 7, 8, 9]
print("Original Array:", arr)

obj.reverseArray(arr, 0, len(arr) - 1)  # Reverse the whole array
print("Reversed Array:", arr)


# Intuition:
# Same logic as Method 1
# Encapsulated in a class to follow OOP style

# Output:
# Original Array: [5, 55, 6, 7, 8, 9]
# Reversed Array: [9, 8, 7, 6, 55, 5]

# TC: O(n) → n = length of array
# SC: O(n) recursion stack



# Method 3 – Reverse a Subarray (Specific Indices)
class Solution:
    def reverseArray(self, arr, left, right):
        if left >= right:  # Base case
            return
        arr[left], arr[right] = arr[right], arr[left]  # Swap
        self.reverseArray(arr, left + 1, right - 1)    # Recursive call

# Example usage
obj = Solution()
arr = [5, 55, 6, 7, 8, 9]
print("Original Array:", arr)

obj.reverseArray(arr, 1, 3)  # Only reverse index 1 to 3 → [55, 6, 7]
print("Reversed Array:", arr)

# Intuition:
# You can reverse any subarray by passing left and right indices
# Only that part of the array will be swapped

# Output:
# Original Array: [5, 55, 6, 7, 8, 9]
# Reversed Array: [5, 7, 6, 55, 8, 9]

# TC: O(r-l+1) → r = right, l = left (size of subarray)
# SC: O(r-l+1) recursion stack
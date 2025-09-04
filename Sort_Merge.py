# Input array
arr = [2,3,8,6,1,4,5,9,4]

# Function to merge two sorted arrays into one sorted array
def merge_array(left, right):
    result = []   # final merged sorted array
    i, j = 0, 0   # pointers for left and right arrays
    n, m = len(left), len(right)

    # Compare elements of both arrays one by one
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])   # smaller element goes into result
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If left array still has elements, append them
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    # If right array still has elements, append them
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result   # return the merged sorted array


# Recursive Merge Sort function
def merge_sort(arr):
    # Base case: if array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]    # left part of the array
    right_half = arr[mid:]   # right part of the array

    # Step 2: Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge_array(left_half, right_half)


# Driver code: calling merge_sort on given array
print(merge_sort(arr))   # Output: [1, 2, 3, 4, 4, 5, 6, 8, 9]



# Time Complexity (TC)------------------------
# Divide array into 2 parts: O(log n) levels recursion
# Merging arrays of size n: O(n) work per level
# Total = O(n log n)
# Best, Average, Worst case = O(n log n)

# Space Complexity (SC)-------------------------
# Extra space for result[] in every merge.
# SC = O(n)

# --------------------------------------------------------------------------------


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # divide left half
    right = merge_sort(arr[mid:])    # divide right half

    result = []                      # merged result
    i = j = 0

    # Merge two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example:
arr = [2,5,6,9,1,3,7,0,4,9,10]
print("Sorted array:", merge_sort(arr))

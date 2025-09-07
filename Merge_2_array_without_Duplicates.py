# -----------two-pointer approach-----merge 2 sorted lists with removing duplicates-----------

nums1 = [1,1,2,4,6,7,9]
nums2 = [1,2,3,6,7,8,10]

# lengths of both lists
n = len(nums1)
m = len(nums2)

# result list where merged unique elements will go
result = []

# two pointers for nums1 and nums2
i = 0
j = 0

# Traverse both arrays until one finishes
while i < n and j < m:
    # if current element of nums1 is smaller or equal
    if nums1[i] <= nums2[j]:
        # check duplicate: add only if result is empty OR last element is different
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    else:
        # else take from nums2
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

# Add remaining elements of nums1 (if any)
while i < n:
    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

# Add remaining elements of nums2 (if any)
while j < m:
    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)



# Time Complexity (TC)--------------------------------
# while i<n and j<m → maximum n+m comparisons
# while i<n + while j<m → remaining elements
# Overall: O(n + m)

# Space Complexity (SC)--------------------------------
# best case: o(1)
# result me worst case n+m elements ho sakte hai → O(n + m) extra space
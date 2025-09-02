# C:\Users\Vishakha\OneDrive\Documents\GitHub\DSA-Python-Questions
nums = [5,7,9,6,5,8,2,3,1,9]

def Selection_sort(nums):
    n = len(nums)
    for i in range(n):
        mini_idx = i
        for j in range(i+1, n):   # yeh loop andar hona chahiye
            if nums[j] < nums[mini_idx]:     # Ascending  Order
           #if nums[j] > nums[mini_idx]:     # Descending Order
                mini_idx = j
        # Swap karna yahin hona chahiye, inner loop ke baad
        nums[i], nums[mini_idx] = nums[mini_idx], nums[i]
    return nums   # sorted list return karna hoga

print(Selection_sort(nums))

# ---------------------------------------------------------

# Selection Sort ke steps simple hai:

# Har step me ek minimum element find karte ho.

# Usko current position ke element se swap karte ho.

# Repeat until list sorted.

# -----------------------------------------------------------------------

# Time Complexity (TC) of Selection Sort

# Selection Sort me:

# Har element ke liye (outer loop n times chalta hai)

# Remaining array scan hoti hai (inner loop approx n-i times chalta hai)

# So total comparisons ≈

# That is O(n²)

# Case wise:

# Best Case: O(n²)
# (even agar array already sorted hai, fir bhi selection sort har element compare karega)

# Average Case: O(n²)

# Worst Case: O(n²)

# Space Complexity (SC)

# Selection Sort in-place sorting algorithm hai (no extra array needed).

# Sirf ek constant space lagta hai swap ke liye.

#  So Space Complexity = O(1)
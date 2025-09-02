nums = [5,1,3,6,8,2,4,9]
n = len(nums)

for i in range(n-1):               # outer loop (n-1 passes)
    for j in range(0, n-1-i):       # inner loop (last i elements already sorted)
        if nums[j] > nums[j+1]:     # swap if out of order
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)



# Optimized Bubble Sort hai jisme ek flag (is_swaped) use kiya gaya hai......


nums = [1,3,5,6,8,9]
n = len(nums)
for i in range(n-1):
    is_swaped=False
    for j in range(0,n-1-i):
        if nums[j]> nums[j+1]:
            nums[j],nums[j + 1] = nums[j+1],nums[j]
            is_swaped = True
    if is_swaped == False:
        break
print(nums)



# Time Complexity (TC)------------------------------------------
# 1. Best Case (Already Sorted List)--------------

# Sirf 1 pass me check ho jata hai, koi swap nahi hota.

# Comparisons = O(n)

# Swaps = 0
#  Best Case TC = O(n)

# 2. Worst Case (Reverse Sorted List)--------------

# Har element ko har pass me compare aur swap karna padta hai.

# Comparisons = n*(n-1)/2 ≈ O(n²)

# Swaps ≈ O(n²)
# Worst Case TC = O(n²)

# 3. Average Case-----------

# Random order me bhi comparisons aur swaps lagbhag n²/2 hote hain.
#  Average Case TC = O(n²)

# Space Complexity (SC)------------------------------------------------

# Bubble sort in-place sorting algorithm hai.

# Extra memory nahi lagta, sirf ek temporary variable for swapping.
#  SC = O(1)


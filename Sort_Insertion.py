nums = [5,4,3,7,8,10,1,9,11]
n = len(nums)
for i in range (1, n ):
    key =nums[i]
    j = i-1
    while j>=0 and nums[j]>key:
        nums[j+1] = nums[j]
        j-=1

    nums[j+1]=key
print(nums)


# -----------------------------------------------------------

# Insertion Sort – Time & Space Complexity
# Time Complexity (TC):

# Best Case (Already Sorted Array):
# Har element sirf ek baar compare hoga, shifting ki zarurat nahi.
# O(n)

# Worst Case (Reverse Sorted Array):
# Har element ko saare pichle elements se compare karna padta hai aur shift karna padta hai.
# Comparisons ≈ 1 + 2 + 3 + ... + (n-1) = n(n-1)/2 ≈ O(n²)

# Average Case:
# On average, half elements shift hote hain.
# O(n²)
# ------------------------------------
# Space Complexity (SC):
# Extra Space Required: Only ek key variable lagta hai insertion ke liye.
# O(1) → Constant extra space.
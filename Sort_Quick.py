# Input array
nums = [4, 1, 2, 6, 3, 7, 1, 0, 8]

# ----------------------------------------------------------
# PARTITION FUNCTION:
# Yahan hum array ko aise todte hain ki pivot se chhote element left me
# aur pivot se bade element right me chale jayein.
# ----------------------------------------------------------
def partition(nums, low, high):
    pivot = nums[low]     # pivot = first element of current subarray
    i = low               # left pointer
    j = high              # right pointer

    # Jab tak i aur j cross nahi karte tab tak loop chalayenge
    while i < j:
        # i ko aage badhao jab tak element pivot se chhota/barabar hai
        while i <= high - 1 and nums[i] <= pivot:
            i += 1
        # j ko peeche lao jab tak element pivot se bada hai
        while j >= low + 1 and nums[j] > pivot:
            j -= 1
        # agar i aur j galat jagah par hain to swap karo
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # Jab loop khatam ho jaye to pivot ko uski sahi jagah par swap karo
    nums[low], nums[j] = nums[j], nums[low]
    return j   # pivot ka correct index return karo

# ----------------------------------------------------------
# QUICK SORT FUNCTION:
# Yahan hum recursively array ko chhote parts me tod kar sort karte hain.
# ----------------------------------------------------------
def quick_sort(nums, low, high):
    if low < high:
        # 1. Array ko partition karo aur pivot ka index lo
        p_idx = partition(nums, low, high)
        # 2. Pivot ke left wale part ko sort karo
        quick_sort(nums, low, p_idx - 1)
        # 3. Pivot ke right wale part ko sort karo
        quick_sort(nums, p_idx + 1, high)

# ----------------------------------------------------------
# DRIVER CODE:
# Pure array par quick_sort call karo
# ----------------------------------------------------------
quick_sort(nums, 0, len(nums) - 1)

print(nums)  # Final sorted array: [0, 1, 1, 2, 3, 4, 6, 7, 8]


# ----------------------------------------------------
# Complexity :-
# TC :- Best / Average Case Time Complexity: O(n log n)
#       Worst Case Time Complexity: O(n²) (jab array already sorted hai aur aap first element ko pivot lete ho)

# SC :- Space Complexity: O(log n) recursion stack
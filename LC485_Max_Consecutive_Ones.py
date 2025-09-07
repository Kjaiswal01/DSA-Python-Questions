nums = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]

# 'count' → ab tak ka current consecutive 1s ka count store karega
count = 0

# 'max_count' → ab tak ka maximum consecutive 1s ka count store karega
max_count = 0

# List ke har element par loop
for i in range(len(nums)):
    # Agar current element 1 hai
    if nums[i] == 1:
        count += 1                 # count badhao
    else:
        # Agar 0 mila to ab tak ka max update karo
        max_count = max(max_count, count)
        count = 0                   # current streak reset karo

# Loop khatam hone ke baad bhi check karo (agar last streak sabse lambi ho)
print(max(max_count, count))


# ------------method name------------
# Ye approach “Kadane’s Algorithm ka variant” hai
# Kadane’s algorithm basically maximum subarray sum nikalta hai, lekin same idea “current streak maintain karo + max update karo” yahan bhi use ho raha hai.
# Isliye isko aksar bolte hain:
# “Sliding Window / Kadane’s-style approach”
# ya phir “Running Count (current + max)” pattern

# Time Complexity:--------------------------------------------
# O(n) → n = list ki length
# Kyunki hum har element ko sirf ek baar traverse karte hain.

# Space Complexity:-----------------------------------------------
# O(1) → humne sirf 2 extra variables (count, max_count) liye hain.
# ----------------Method 1 (Brute Force)-------------------------
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)

# maxi stores the maximum subarray sum found so far
maxi = float("-inf")  # initially -infinity so any sum will be larger

# Outer loop chooses the start index of subarray
for i in range(0,n):
    total = 0   # will store sum of current subarray starting at i

    # Inner loop chooses the end index of subarray
    for j in range(i,n):
        total = total + nums[j]  # add next element to current subarray sum
        maxi = max(maxi,total)   # update maxi if current sum > maxi

print(maxi)  # Final maximum subarray sum


# Idea:Har possible subarray ka sum nikal kar maximum choose karo.
# Time Complexity (TC): O(n²)----------------
# (outer loop n times × inner loop ~n times)

# Space Complexity (SC): O(1)----------------
# (extra variables only)



# ----------------Method 2 (Kadane’s Algorithm — Optimized)--------------------------------------------
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)

# maxi stores maximum subarray sum so far
maxi = float("-inf")
# total stores current subarray sum
total = 0 

# Single pass through array
for i in range(0,n):
    total = total + nums[i]      # extend current subarray by nums[i]
    maxi = max(maxi, total)      # update maxi if current sum > maxi
    if total < 0:                # if sum becomes negative, reset to 0
        total = 0                # start new subarray from next index

print(maxi)

# Positive energy carry karo, negative energy chhod do; har step pe best yaad rakho
# Idea:Running sum ko carry karte raho.
# Agar sum negative ho gaya to wo future me kisi subarray ko sirf chhota karega, isliye reset kar do.
# Ye hi Kadane’s Algorithm hai.

# Time Complexity (TC): O(n)--------------
# (single loop)

# Space Complexity (SC): O(1)-------------
# (only a couple of variables)
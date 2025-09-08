# -----------------Brute Force Method (O(n^2))------------------------------
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
max_count = 0

for i in range(n):                       # pick each number as starting point
    num = nums[i]
    count = 1
    while num + 1 in nums:               # check next consecutive number in list (O(n))
        count += 1
        num = num + 1
    max_count = max(max_count, count)    # update maximum length

print(max_count)  # Output: 4


# Idea: Har element se start karke check karo num+1 present hai ya nahi.

# Time Complexity:------- Outer loop O(n) × membership check O(n) = O(n²)
# Space Complexity:------ O(1) (no extra data structure)

 




# ---------------------Sorting Method (O(n log n)-------------------
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
nums.sort()                             # sort numbers first
count = 0
last_smallest = float("-inf")           # track previous number
longest = 0

for i in range(n):
    num = nums[i]
    if num - 1 == last_smallest:        # consecutive number
        count += 1
        last_smallest = num
    elif num != last_smallest:          # new sequence (skip duplicates)
        count = 1
        last_smallest = num
    longest = max(longest, count)       # update maximum length

print(longest)  # Output: 4


# Idea: Numbers ko sort karo, phir consecutive numbers count karo.

# Time Complexity:----- Sorting O(n log n) + single pass O(n) = O(n log n)

# Space Complexity:---- O(1) (apart from sorting’s internal use)






# ---------------------Optimal Method using HashSet (O(n))------------------------
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)

# Step 1: Put all numbers in a set for O(1) membership checks
my_set = set()
for i in range(n):
    my_set.add(nums[i])

longest = 0

# Step 2: Only start counting when number is start of a sequence
for num in my_set:
    if num - 1 not in my_set:           # start of a new sequence
        x = num
        count = 1
        while x + 1 in my_set:          # check next numbers in sequence
            count += 1
            x += 1
        longest = max(longest, count)   # update maximum length

print(longest)  # Output: 4


# Idea:
# Membership check O(1) with set.
# Only start counting at the start of sequence (num-1 not present).
# This gives O(n) total time.

# Time Complexity:------- O(n) (build set + loop through set)

# Space Complexity:------ O(n) (extra set)


# nums = [[5,20,3],[7,-10,9],[1,-52,6]]
# rows = len(nums)
# cols = len(nums)
# for i in range(0,rows):
#     for j in range(0,cols):
#         print(nums[i][j],end="  ")
# print()

# nums = [[5,20,3],[7,10,9],[1,-52,6]]
# rows = len(nums)
# cols = len(nums)
# for i in range(0,rows):
#     for j in range(0,cols):
#         if j>=i:
#             print(nums[i][j],end="  ")
#         else:
#             print("*",end ="   ")
#     print()

# nums = [[5,20,3],[7,10,9],[1,-52,6]]
# rows = len(nums)
# cols = len(nums)
# for i in range(0,rows):
#     for j in range(0,cols):
#         if i>=j:
#             print(nums[i][j],end="  ")
#         else:
#             print("*",end ="   ")
#     print()
    
# nums = [[5,20,3],
#         [7,10,9],
#         [1,-52,6]]
# rows = len(nums)
# cols = len(nums[0])          # number of columns
# for i in range(rows):
#     for j in range(cols):
#         # condition for secondary diagonal: i + j == cols - 1
#         if i + j == cols - 1:
#             print(nums[i][j], end="  ")
#         else:
#             print("*", end="   ")
#     print()                  # new line after each row

# nums = [[5,20,3],
#         [7,10,9]]
# rows = len(nums)
# cols = len(nums[0])          # number of columns
# result = [[0]*rows for i in range(cols)]
# for i in range(0,rows):
#     for j in range(0,cols):
#         result[j][i] = nums[i][j]
# print(result)

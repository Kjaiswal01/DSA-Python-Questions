# Method 1 – Brute Force (linear Srch) (Check each number in the list)
# Idea: 0 se n tak ke saare numbers check karo ki vo nums me hai ya nahi

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)

for i in range(0, n + 1):             # 0 se n tak iterate karo
    if i not in nums:                 # Agar i nums me nahi hai
        print(i)                      # Vo missing number hai

# Time Complexity: O(n²) (kyunki i not in nums har baar O(n) time leta hai)
# Space Complexity: O(1) (koi extra array nahi use kar rahe)

# ----------------------------------------------------------------------------------------------

# Method 2 – Frequency Dictionary (Hash Map)
# Idea: 0 se n tak ek dict me frequency store karo, phir jiski frequency 0 ho vo missing hai

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)

freq = {}                              # 0 se n tak frequency dictionary banao
for i in range(0, n + 1):
    freq[i] = 0                        # sabhi numbers initially 0 frequency

for num in nums:
    freq[num] = 1                      # jo number array me present hai uski frequency 1 karo

for k, v in freq.items():
    if v == 0:                         # jis number ki frequency 0 hai vo missing hai
        print(k)
        
# Time Complexity: O(n) (dictionary banane + fill karne + check karne me total linear time)
# Space Complexity: O(n) (dictionary/frequency array banane ki wajah se extra space)
        
# ----------------------------------------------------------------------------------------------------------       
        
# Method 3 – Optimal (Using Sum Formula)
# Idea: 0 se n tak numbers ka sum n*(n+1)//2 hota hai.
# Missing number = (expected sum) - (actual sum of nums)

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)

missing = n * (n + 1) // 2 - sum(nums)  # Expected sum - actual sum
print(missing)

# Time Complexity: O(n) (sirf sum(nums) nikalne me linear time lagta hai)
# Space Complexity: O(1) (koi extra space nahi use kar rahe)       
        
             
# Method 1 – Digit Extraction using % and //
# Goal: Extract each digit of a number from last to first
n = 5873
num = n

while num > 0:
    last_digit = num % 10  # %10 gives last digit of the number
    print(last_digit)      # print the last digit
    num = num // 10        # //10 removes the last digit
    
# Time Complexity (TC): O(d) → d = number of digits
# Space Complexity (SC): O(1) (extra variables only)



# Method 2 – Counting Digits Iteratively
# Goal: Count how many digits a number has
n = 587364852
num = n
count = 0

while num > 0:
    count += 1       # increment count for each digit
    num = num // 10  # remove last digit

print(count)  # prints total number of digits

# Intuition:
# Each iteration removes one digit
# Count increments → total digits
# Stop when number becomes 0
# Output: 9

# TC: O(d) → d = number of digits
# SC: O(1)





# Method 3 – Using Mathematical Formula (log10)
from math import log10

def count_digits(num):
    # log10(num) gives power of 10 (position of first digit)
    # +1 because digit count = floor(log10(num)) + 1
    return int(log10(num) + 1)

print(count_digits(587364852))


# Intuition:
# log10(1000) = 3 → number has 4 digits → formula: floor(log10(num)) + 1
# Works only for positive integers
# Output:9

# TC: O(1) → constant time (no loops)
# SC: O(1)
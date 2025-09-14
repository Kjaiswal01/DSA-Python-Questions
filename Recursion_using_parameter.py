# Method 1 – Print x, n times------------------------------------

def func(x, n):
    if n == 0:   # Base case: stop when no more repetitions left
        return
    print(x)     # Print x
    func(x, n-1) # Recursive call with n-1

func(15, 4)


# Output:   # 15
            # 15
            # 15
            # 15


# Intuition:
# Print the value
# Reduce n → recursion handles repetition

# TC: O(n) → n = number of times to print
# SC: O(n) recursion stack



# Method 2 – Print 1 to N using Recursion (Head Recursion)-----------------------------------
def func(i, n):
    if i > n:    # Base case: stop when i exceeds n
        return
    print(i)    # Print current number
    func(i+1, n)  # Recursive call with next number

func(1, 7)




#Output # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7


# Intuition (Head Recursion):
# Print before recursive call → numbers printed in ascending order

# TC: O(n) → n = upper limit
# SC: O(n) recursion stack



# Method 3 – Print N to 1 using Recursion (Head Recursion)---------------------------------------------
def func(n):
    if n == 0:
        return
    print(n)      # Print current number first
    func(n-1)     # Recursive call with n-1

func(7)


# Output:   # 7
            # 6
            # 5
            # 4
            # 3
            # 2
            # 1


# Intuition:
# Head recursion prints before recursive call → descending order

# TC: O(n)
# SC: O(n)



# Method 4 – Print N to 1 using Tail Recursion--------------------------------------------------
def func(i, n):
    if i > n:   # Base case
        return
    func(i+1, n)  # Recursive call first
    print(i)       # Print after recursion

func(1, 7)


# Output:   # 7
            # 6
            # 5
            # 4
            # 3
            # 2
            # 1

# Intuition (Tail Recursion):
# Recursive call first → print after recursion → descending order
# Can be visualized as stack unwinding

# TC: O(n)
# SC: O(n)




# Method 5 – Sum of 1 to N using Recursion-----------------------------------------------------
def func(sum, i, n):
    if i > n:        # Base case: when i exceeds n
        print(sum)   # Print accumulated sum
        return
    func(sum + i, i + 1, n)  # Add current i to sum and move to next

func(0, 1, 10)


# Output:55

# Intuition:
# Accumulate sum as recursion progresses
# Base case prints final result

# TC: O(n) → n = upper limit
# SC: O(n) recursion stack
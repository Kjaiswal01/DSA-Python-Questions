
# Optimal Method (Using Row & Col Track Arrays)
# Input matrix
matrix = [[5,20,9,3],
          [7,2,0,9],
          [1,0,3,9],
          [1,2,4,6]]

r = len(matrix)
c = len(matrix[0])

# Step 1: Make arrays to keep track of which rows/cols have zero
rowtrack = [0 for _ in range(r)]
coltrack = [0 for _ in range(c)]

# Step 2: Mark rowtrack & coltrack where zeros are found
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j] == 0:
            rowtrack[i] = -1       # mark row i to be zeroed
            coltrack[j] = -1       # mark col j to be zeroed

# Step 3: Update matrix based on rowtrack & coltrack
for i in range(0,r):
    for j in range(0,c):
        if rowtrack[i] == -1 or coltrack[j] == -1:
            matrix[i][j] = 0

# Print final matrix
for row in matrix:
    print(row)

# Explanation:
# Pehle pass me hum sirf mark karte hain ki kaun-si row/column zero honi chahiye (rowtrack & coltrack arrays)
# Dusre pass me us hisaab se matrix ko update karte hain.
# Isme koi infinity mark karne ka chakkar nahi hai, isliye efficient hai.

# Time Complexity (TC):------------------------------
# Pehla loop: matrix traverse = O(r * c)
# Dusra loop: matrix traverse = O(r * c)
# Total = O(r * c)
# (Much better than brute force)

# Space Complexity (SC):-------------------------------
# Extra arrays rowtrack (size r) & coltrack (size c) = O(r + c) extra space
# Still quite efficient.




# Brute Force Method (Using markInfinity)-----------------------------------------------------------
# Input matrix
matrix = [[5,20,9,3],
          [7,2,0,9],
          [1,0,3,9],
          [1,2,4,6]]

# r = no. of rows, c = no. of columns
r = len(matrix)
c = len(matrix[0])

# Step 1: Helper function to mark entire row & column as infinity when a zero is found
def markInfinity(matrix, row , col):
    # Mark column as infinity (skip original zeros)
    for i in range(0, len(matrix)):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")
    # Mark row as infinity (skip original zeros)
    for j in range(0, len(matrix[0])):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")

# Step 2: Main function to set zeros in matrix
def setZeros(matrix) -> None:
    r = len(matrix)
    c = len(matrix[0])
    # First pass: whenever a zero is found, mark its row & column as infinity
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                markInfinity(matrix, i, j)
    # Second pass: replace all infinities with zero
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

# Call function
setZeros(matrix)

# Print the final matrix
for row in matrix:
    print(row)

# Explanation:
# Pehle loop me jab bhi 0 milta hai, uski row aur column ko ∞ (float("inf")) se mark kar dete hain (taaki baad me identify kar sake).
# Dusre loop me saare ∞ ko actual 0 me convert kar dete hain.

# Time Complexity (TC):-------------------------------
# markInfinity har 0 ke liye O(r + c) ka kaam karega
# Worst case: saari cells check + saari rows/columns mark
# = O(r * c * (r + c))
# Yeh brute force hai, kaafi heavy hai.

# Space Complexity (SC):---------------------------
# Humne extra array nahi banaya, sirf float("inf") use kiya
# = O(1) extra space
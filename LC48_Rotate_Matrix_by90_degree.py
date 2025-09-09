# ---(optimal)------------In-place Method (Transpose + Reverse)---------------------
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

n = len(matrix)

# --- Step 1: Transpose the matrix in-place ---
# Transpose means: convert rows to columns
# i.e. swap matrix[i][j] with matrix[j][i] for j>i
for i in range(n):
    for j in range(i+1,n):      # only upper triangle swap
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

# After transpose:
# [1,5,9,13]
# [2,6,10,14]
# [3,7,11,15]
# [4,8,12,16]

# --- Step 2: Reverse each row ---
# Reversing each row gives us a 90° clockwise rotation
for i in range(n):
    matrix[i].reverse()

# Final matrix after rotation:
# [13, 9, 5, 1]
# [14,10, 6, 2]
# [15,11, 7, 3]
# [16,12, 8, 4]

# Print the rotated matrix
for row in matrix:
    print(row)


# Kya ho raha hai?
# Transpose karne se rows → columns ho jaati hain
# Fir har row reverse karne se wo 90° clockwise rotate ho jaata hai

# Time Complexity (TC):-------------
# Transpose loop → O(n²)
# Reverse each row → O(n²)
# Overall: O(n²)

# Space Complexity (SC):-------------
# Sab kuch in-place hota hai → O(1) extra space




# ----------------Brute Force Method (New Result Array)---------------------------------------------
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

n = len(matrix)

# Create an empty n x n matrix for result
result = [[0 for _ in range(n)] for _ in range(n)]

# Fill result such that result[j][n-1-i] = matrix[i][j]
# This directly places element in its rotated position
for i in range(n):
    for j in range(n):
        result[j][(n-1)-i] = matrix[i][j]

# Print the rotated matrix
for row in result:
    print(row)


# Kya ho raha hai?
# Har element ko directly uske 90° rotated index me daal dete hain (new array me)
# Formula: result[column][n-1-row] = matrix[row][column]

# Time Complexity (TC):---------------------
# Double loop → O(n²)

# Space Complexity (SC):-----------------
# New n x n matrix banai hai → O(n²) extra space
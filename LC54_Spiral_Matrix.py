# (Using Class & Object)

from typing import List

# Define a class Solution
class Solution:
    # Define method spiralOrder to return elements of matrix in spiral order
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Edge case: if matrix is empty or first row is empty, return empty list
        if not matrix or not matrix[0]:
            return []

        # This will store our spiral order result
        result = []

        # Initialize four boundary pointers
        top, left = 0, 0                            # top row index, left column index
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1   # bottom row index, right column index

        # Loop until all layers are processed
        while top <= bottom and left <= right:

            # 1. Traverse from left to right across the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1   # top row has been processed, move boundary down

            # 2. Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # right column processed, move boundary left

            # 3. Traverse from right to left across the bottom row (only if still within bounds)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # bottom row processed, move boundary up

            # 4. Traverse from bottom to top along the left column (only if still within bounds)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # left column processed, move boundary right

        # Return the spiral order list
        return result

# your matrix---------------------------------------------
matrix = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11]
]

# create object of the class
sol = Solution()

# call the method and print the result
output = sol.spiralOrder(matrix)
print(output)


# How this works (Intuition):-----------
# Imagine peeling layers from an onion.
# First take the top row left→right.
# Then take the right column top→bottom.
# Then the bottom row right→left.
# Then the left column bottom→top.
# Shrink the boundaries (top, bottom, left, right) after each step, and repeat until you’ve visited all elements.

# Time Complexity (TC):-----------------------
# We visit each element exactly once.
# For an m x n matrix: O(m * n)

# Space Complexity (SC):----------------------------
# Output list result stores all elements → O(m * n)
# Extra variables (top, bottom, left, right) are O(1)
# So total auxiliary (extra) space: O(1) (ignoring output)
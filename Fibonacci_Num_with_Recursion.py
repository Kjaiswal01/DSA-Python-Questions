# Find the Fibonacci n using recursion ---------------------------------------------

class Solution :
    def func(self,num):
        if num==0 or  num==1:
            return num 
        return self.func(num-1) + self.func(num-2)
    def fib(self,n:int)->int:
        result= self.func(n)
        return result
# Example
s = Solution()
print(s.fib(20))  # 6765    # Recursive: slow (O(2^n))


# take input from user --------------------------------------------------------------
class Solution:
    def func(self, num):
        if num == 0 or num == 1:   # yaha or hona chahiye
            return num
        return self.func(num - 1) + self.func(num - 2)

    def fib(self, n: int) -> int:
        result = self.func(n)
        return result

# Example with user input
s = Solution()
n = int(input("Enter a number: "))   # user se input le raha hai      #Enter a number: 10

print(f"Fibonacci of {n} is:", s.fib(n))    # Fibonacci of 10 is: 55

# --------------------------------------------------------------------------------------------------------------------------------


# 🔹 Iterative Fibonacci Method (Best for Interviews)
def fibonacci(n):
    if n==0 or n==1:
        return n
    
    a, b = 0, 1   # pehle do numbers set kar diye
    for i in range(2, n + 1):
        a, b = b, a + b   # update karte gaye
    return b

print(fibonacci(10))  # Output: 55   
# Iterative: fast (O(n), O(1) space)



# Fibonacci sequence mein har element apne last two elements ka sum hota hai.
# Recursive solution toh hota hai, lekin wo inefficient hai because same values bar-bar compute hoti hain.
# Best approach iterative hai, jisme main sirf do variables rakhta hoon aur loop mein unhe update karta hoon.
# Iska time complexity O(n) hai aur space O(1), jo sabse efficient hai.

# Key Points Yaad Rakhne ke liye (Interview Trigger Lines)

# Fibonacci: next = previous two ka sum

# Real life analogy: two runners on a track, each new runner is sum of last two
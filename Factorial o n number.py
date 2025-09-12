# time complexity -> o(n)
# space complexity -> o(n)--> stack space

def fact(num):
    if num==0 or num== 1:
        return 1
    return num*fact(num-1)
print(fact(4))

class Solution:
    def func(self, num):
        if num == 1 or num == 0:
            return 1
        return num * self.func(num - 1)

obj = Solution()
print(obj.func(5))


# Fibonacci Number
# F(n) = F(n - 1) + F(n - 2)
# Given n, calculate F(n)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


obj = Solution()
print(obj.fib(9))

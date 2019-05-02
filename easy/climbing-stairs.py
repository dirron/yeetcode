# Problem 70: Climbing stairs (done recursively as part of lesson)
# this is basically fibonacci
class Solution:
    sols = {}
    def climbStairs(self, n: int) -> int:
        if n in self.sols:
            return self.sols[n]
        if n == 0 or n == 1 or n == 2:
            self.sols[n] = n
            return n
        self.sols[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.sols[n]
# Problem 9: without string conversion
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        ans = 0
        temp_x = x
        while temp_x >= 1:
            ans = ans * 10
            ans += temp_x % 10
            temp_x = int(temp_x / 10)
        
        return x - ans == 0
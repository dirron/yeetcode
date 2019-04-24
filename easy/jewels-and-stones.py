# Problem 771
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = []
        total = 0
        
        for j in J:
            jewels.append(j)
        
        for jewel in S:
            if jewel in jewels:
                total += 1
            
        return total
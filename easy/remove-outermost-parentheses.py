# Problem 1021
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        output = ""
        
        count = 0
        started = False
        
        for c in range(len(S)):
            a = 0

            if count == 0 and not started:
                started = True
                a += 1
                
            if S[c] == '(':
                count += 1
            elif S[c] == ')':
                count -= 1

            if count == 0 and started:
                started = False
                a += 1
            
            if a == 0:
                output += S[c]
        
        return output
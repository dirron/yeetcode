# Problem 559: Max depth of n-ary tree

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        S = []
        S.append((root, 0))
        seen = set()
        max = 0
        
        while S:
            v, depth = S.pop()
            
            if v is not None:
                depth += 1
            else:
                continue
            
            if depth > max:
                max = depth
            
            if v not in seen:
                seen.add(v)
                for child in v.children:
                    S.append((child, depth))
        
        return max
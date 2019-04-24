import math

# Problem 103
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        else:
            return 'None'
        return str(self.val)

def BFS_zigzag(v: TreeNode):
    if v is None:
        return []

    output = [[v.val]]
    S = []
    tree_index = 1
    S.append((v, 1))
    prev_depth = 0
    
    while S:
        tree_index += 2
        v, depth = S.pop(0)

        if depth > prev_depth:
            output.append([])

        children = []
        
        if (v.val == -1):
            print(-1, 'depth =', depth)

        if v.left is not None and v.left.val is not None:
            children.append(v.left)
        if v.right is not None and v.right.val is not None:
            children.append(v.right)
        
        for child in children:
            S.append((child, depth + 1))
        
        for child in children:
            if (depth + 1) % 2 != 0:
                output[-1].append(child.val)
            else:
                output[-1].insert(0, child.val)
        
        prev_depth = depth
            
    return (list(filter(lambda a: a != [], output)))

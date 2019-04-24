import math


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

    output = [[v.val],[]]
    S = []
    tree_index = 1
    S.append(v)
    S.append(None)
    depth = 1
    
    while S:
        tree_index += 2
        v = S.pop(0)

        if v is None:
            depth += 1
            S.append(None)
            output.append([])
            
            if S[0] is None:
                break
            else:
                continue

        children = []

        if v.left is not None and v.left.val is not None:
            children.append(v.left)
        if v.right is not None and v.right.val is not None:
            children.append(v.right)
        
        for child in children:
            S.append(child)
        
        print(depth)
        if (depth + 1) % 2 == 0:
            children.reverse()
        
        for child in children:
            output[-1].append(child.val)
            
    return (list(filter(lambda a: a != [], output)))

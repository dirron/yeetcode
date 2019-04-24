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

    output = [v.val]
    S = []
    tree_index = 1
    S.append(v)
    
    while S:
        tree_index += 2
        depth = math.floor(math.log(tree_index)) + 1
        v = S.pop(0)

        children = []

        if v.left is not None: # and v.left.val is not None:
            children.append(v.left)
        if v.right is not None: # and v.right.val is not None:
            children.append(v.right)
        
        if depth % 2 == 0:
            children.reverse()
        
        for child in children:
            S.append(child)
            output.append(child.val)
    
    return output

input = [1,2,None,3,None,4,None,5]
tree = []
last_not_none = None
for i, val in enumerate(input):
    child = TreeNode(val)
    
    tree.append(child)

    if i > 0:
        parent = tree[math.floor((i - 1) / 2)]

        if parent.val is None:
            parent = last_not_none

        if parent.left is None:
            parent.left = child
        else:
            parent.right = child
            
    if child.val is not None:
        last_not_none = child

print('Tree = ', tree)
print('Output = ', BFS_zigzag(tree[0]))

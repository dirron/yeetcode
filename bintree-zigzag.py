class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BFS(v: TreeNode):
    output = []
    
    S = []
    depth = 1
    count = 0
    
    output.append([v.val])
    S.append(v)
    
    toRight = False
    pair = []
    while S:
        
        cur = S.pop(0)
        adj = []
        
        if cur.left is not None or cur.right is not None:
            if toRight:
                adj = [cur.left, cur.right]
            else:
                adj = [cur.right, cur.left]

            for w in adj:
                if w is not None and w.val is not None:
                    pair.append(w.val)
                    w.val = None
                    S.append(w)
                    count += 1
            
            if pair:
                output.append(pair)
                if len(pair) == 2:
                    pair = []
        
        if count > 2 ** (depth - 1):
            toRight = not toRight
            depth += 1
    
    return output

a1 = TreeNode(1)
a2 = TreeNode(2)

a1.left = a2

print(BFS(a1))
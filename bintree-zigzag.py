class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def should_incr_depth(count, cur_depth) -> bool:
    return count > (2 ** (cur_depth - 1))

def BFS(v: TreeNode):

    output = []
    
    S = []
    depth = 1
    count = 0
    pair = []
    to_right = True

    output.append([v.val])
    S.append(v)
    
    while S:
        prev_depth = depth
        cur = S.pop(0)
        adjacent = []

        if should_incr_depth(count, depth):
            depth += 1
            to_right = not to_right
        
        print(cur.val, ' ', depth, ' ', count, ' ', to_right)
                
        if to_right:
            adjacent = [cur.left, cur.right]
        else:
            adjacent = [cur.right, cur.left]

        for w in adjacent:
            if w is not None and w.val is not None:
                pair.append(w.val)
                w.val = None
                S.append(w)
            count += 1
        
        if pair:
            output.append(pair)
            if len(pair) == 2 or (prev_depth < depth):
                pair = []
    
    return output

tree = []
for i in range(5):
    
    tree.append(TreeNode(i + 1))

tree[0].left = tree[1]
tree[0].right = tree[2]
tree[1].left = tree[3]
tree[1].right = tree[4]

print(BFS(tree[0]))
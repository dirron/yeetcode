from typing import List
import collections


'''
Islands are connected by having the same row or column (not by actually being next to each other).
With that in mind, islands have 1 element that can be left behind while the rest is removed.
Then the answer to the problem is in fact the number of stones minus the number of islands.
'''
def removeStones(stones: List[List[int]]) -> int:
    def DFS(i, j):
        # remove the seen points so that we can count the islands
        points.discard((i, j))
        
        # traverse to other parts of island
        for y in rows[i]:
            if (i, y) in points:
                DFS(i, y)
        for x in cols[j]:
            if (x, j) in points:
                DFS(x, j)
    
    points = {(i, j) for i, j in stones}
    island = 0
    rows = collections.defaultdict(list)
    cols = collections.defaultdict(list)
    
    # store the rows/cols to be checked as a neighbour (part of an island) by DFS
    for i, j in stones:
        rows[i].append(j)
        cols[j].append(i)
    
    # perform DFS on each island and count the number of islands
    for i, j in stones:
        if (i, j) in points:
            DFS(i, j)
            island += 1
    
    
    return len(stones) - island

print(removeStones([[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]))
from typing import List

# Problem 454: 4Sum II

def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    count = 0
    table = {}

    for a in A:
        for b in B:
            if a + b in table:
                table[a+b] += 1
            else:
                table[a+b] = 1
    
    # for each c in C and D in D, if -c and -d have been seen then c + d - c - d = 0
    for c in C:
        for d in D:
            if -c - d in table:
                count += table[-c - d]

    return count

print(fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))

from typing import List


# Problem 119: Pascal's Triangle II (done recursively as part of lesson)
def getRow(rowIndex: int) -> List[int]:
    def pasc(cur: int, rowIndex: int, row: List[int]):
        if cur > rowIndex:
            return row
        for i in reversed(range(cur)):
            if i == 0 or i == cur-1:
                row[i] = 1
            else:
                row[i] = row[i] + row[i-1]

        pasc(cur+1, rowIndex, row)

    row = [0]*rowIndex
    pasc(0, rowIndex, row)
    return row


print(getRow(23))

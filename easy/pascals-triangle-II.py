# Problem 119: Pascal's Triangle II (done recursively as part of lesson)
def pascal_num(i: int, j: int, triangle):
    if j == 1 or j == i:
        triangle[i-1][j-1] = 1
        return 1
    elif triangle[i-1][j-1] != 0:
        return triangle[i-1][j-1]

    sol = pascal_num(i - 1, j - 1, triangle) + pascal_num(i - 1, j, triangle)
    triangle[i-1][j-1] = sol
    return sol


def getRow(rowIndex: int):
    row = [[0]*i for i in range(1, rowIndex + 1)]
    for i in range(1, rowIndex + 1):
        row[rowIndex-1][i-1] = pascal_num(rowIndex, i, row)

    return row[rowIndex-1]


print(getRow(5))

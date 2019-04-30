# Problem 118: Pascal's Triangle (done recursively as part of lesson)
def pascal_num(i: int, j: int, triangle):
    if j == 1 or j == i:
        triangle[i-1][j-1] = 1
        return 1
    elif triangle[i-1][j-1] != 0:
        return triangle[i-1][j-1]

    sol = pascal_num(i - 1, j - 1, triangle) + pascal_num(i - 1, j, triangle)
    triangle[i-1][j-1] = sol
    return sol


def generate(numRows: int):
    triangle = [[0]*i for i in range(1, numRows + 1)]
    for i in range(1, numRows + 1):
        for j in range(1, i + 1):
            triangle[i - 1][j - 1] = pascal_num(i, j, triangle)

    return triangle


print(generate(5))

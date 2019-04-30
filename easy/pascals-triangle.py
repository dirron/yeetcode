# Problem 118: Pascal's Triangle (done recursively as part of lesson)
def pascal_num(i: int, j: int, sols):
    if j == 1 or j == i:
        sols[(i, j)] = 1
        return 1
    elif (i, j) in sols:
        return sols[(i, j)]

    sol = pascal_num(i - 1, j - 1, sols) + pascal_num(i - 1, j, sols)
    sols[(i, j)] = sol
    return sol


def generate(numRows: int):
    sols = {}

    ans = []
    for i in range(1, numRows + 1):
        ans.append([])
        for j in range(1, i + 1):
            ans[-1].append(pascal_num(i, j, sols))

    return ans


print(generate(5))

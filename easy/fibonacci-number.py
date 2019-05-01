# Problem 509: Fibonacci Number (done recursively as part of lesson)
F = {}
def fib(N: int) -> int:
    if N in F:
        return F[N]
    if N == 0 or N == 1:
        F[N] = N
        return N
    F[N] = fib(N-1) + fib(N-2)
    return F[N]

print(fib(6))
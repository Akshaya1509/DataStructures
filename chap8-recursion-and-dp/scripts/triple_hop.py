# Script to check how many ways child will run in n steps in a staircase

def n_steps(n, memo):
    # print(n)
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = n_steps([n-1][0], memo) + n_steps([n-2][0], memo) + n_steps([n-3][0], memo)
    return memo[n]

if __name__ == "__main__":
    memo = {}
    print(n_steps(10, memo))
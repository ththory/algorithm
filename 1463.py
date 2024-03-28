import sys
def makeOne(X):
    dp = [0] * (10**6 + 1)
    for i in range(1, X + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    return dp[X] - 1
N = int(sys.stdin.readline().rstrip())
print(makeOne(N))




# A1. Tree 형태로 모두 탐색.
# def makeOne(X, count):
#     if X == 1: return count
#     result = [makeOne(X - 1, count + 1)]
#     if X % 3 == 0:
#         result.append(makeOne(X // 3, count + 1))
#     if X % 2 == 0:
#         result.append(makeOne(X // 2, count + 1))
#     return min(result)
#
# N = int(sys.stdin.readline().rstrip())
# print(makeOne(N, 0))
def countWays(B, weights, N):
    dp = [0] * (B + 1)
    dp[0] = 1

    for i in range(N):
        for j in range(B, weights[i] - 1, -1):
            dp[j] += dp[j - weights[i]]

    return dp[B]

B = int(input())
N = int(input())

weights = []
for _ in range(N):
    weight = int(input())
    weights.append(weight)

result = countWays(B, weights, N)
print(result)

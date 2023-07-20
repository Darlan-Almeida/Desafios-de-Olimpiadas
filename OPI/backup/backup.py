# n -> numero de elementos no array
# l -> inicio do intervalo
# r -> fim do intervalo

MOD = 10**9 + 7

def count_arrays(n, l, r):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(3):
            for x in range(l, r + 1):
                print("j" , j)
                print("x" , x)
                print((j - x + 3) % 3)
                dp[i][j] += dp[i-1][(j - x + 3) % 3]


    return dp[n][0] % MOD

n, l, r = map(int, input().split())
result = count_arrays(n, l, r)
print(result)
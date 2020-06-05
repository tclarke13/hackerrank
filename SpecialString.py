def substrCount(n, s):
    dp = []
    P = []

    for i in range(n):
        dp.append([0 for j in range(n)])
        P.append([False for j in range(n)])

    for i in range(n):
        dp[i][i] = 1
        P[i][i] = True

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap

            if gap % 2:
                if s[j] == s[j - 1]:
                    if gap > 1:
                        if P[i][j - 2] and s[j - 1] == s[j - 2]:
                            P[i][j] = True
                    else:
                        P[i][j] = True
            else:
                if P[i + 1][j - 1] and s[i] == s[j]:
                    if gap == 2 or (gap > 2 and s[j] == s[j - 1]):
                        P[i][j] = True

            dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]

            if P[i][j]:
                dp[i][j] += 1

    for i in range(n):
        print(P[i])
        print(dp[i])
    return dp[0][n-1]


if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline())

        s = f.readline()

        result = substrCount(n, s)

        print(str(result) + "\n")

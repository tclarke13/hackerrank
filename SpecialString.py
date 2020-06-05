def substrCount(n, s):
    dp = []
    P = []

    for i in range(n):
        dp.append([0 for j in range(n)])
        P.append([False for j in range(n)])

    for i in range(n):
        dp[0][i] = 1
        dp[i][0] = 1
        P[0][i] = True
        P[i][0] = True

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = 1
            P[i][j] = False

    



if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline())

        s = f.readline()

        result = substrCount(n, s)

        print(str(result) + "\n")

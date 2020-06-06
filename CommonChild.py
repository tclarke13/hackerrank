def commonChild(s1, s2):
    dp = []
    for i in range(len(s1)):
        dp.append([0 for elem in s2])
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = 1

    for list in dp:
        print(list)

    for length in range(1, min(len(s1), len(s2))):
        new_dp = []
        for i in range(len(s1) - length):
            new_dp.append([0 for elem in range(len(s2) - length)])
            for j in range(len(s2) - length):
                extra_match_before = 1 if s1[i] == s2[j] else 0
                extra_match_after = 1 if s1[i+length] == s2[j+length] else 0
                new_dp[i][j] = max(dp[i][j] + extra_match_after, dp[i+1][j], dp[i][j+1], dp[i+1][j+1] + extra_match_before)

        dp = new_dp

        print("")
        for list in new_dp:
            print(list)

    return dp[0][0]

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        s1 = f.readline().split("\n")[0]

        s2 = f.readline().split("\n")[0]

        result = commonChild(s1, s2)

        print(str(result) + "\n")

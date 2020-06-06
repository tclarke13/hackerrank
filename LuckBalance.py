def luckBalance(k, contests):
    totalLuck = 0
    numImportantLost = 0

    contests.sort(reverse=True, key = lambda i : i[0])

    for contest in contests:
        if contest[1] == 0:
            totalLuck += contest[0]
        else:
            if numImportantLost >= k:
                totalLuck -= contest[0]
            else:
                totalLuck += contest[0]
                numImportantLost += 1

    return totalLuck



if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        nk = f.readline().rstrip().split()

        n = int(nk[0])

        k = int(nk[1])

        contests = []

        for _ in range(n):
            contests.append(list(map(int, f.readline().rstrip().split())))

        result = luckBalance(k, contests)

        print(str(result) + "\n")

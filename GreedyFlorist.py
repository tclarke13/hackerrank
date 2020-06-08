def getMinimumCost(c, k):
    c.sort(reverse=True)
    cost = 0
    for i in range(len(c)):
        cost += c[i] * (1 + i // k)

    return cost



if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        nk = f.readline().rstrip().split()

        n = int(nk[0])

        k = int(nk[1])

        c = list(map(int, f.readline().rstrip().split()))

        minimumCost = getMinimumCost(c, k)

        print(str(minimumCost) + "\n")

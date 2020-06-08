def getMinimumCost(k, c):



if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        c = list(map(int, input().rstrip().split()))

        minimumCost = getMinimumCost(k, c)

        print(str(minimumCost) + "\n")

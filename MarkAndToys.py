def maximumToys(prices, k):
    sortedPrices = sorted(prices)
    total = 0
    numItems = 0
    for price in sortedPrices:
        if total + price <= k:
            numItems += 1
            total += price
        else:
            break
    return numItems

if __name__ == '__main__':

    infile = "Input//MarkAndToys.txt"
    with open(infile, 'r') as f:
        nr = f.readline().rstrip().split()

        n = int(nr[0])

        r = int(nr[1])

        arr = list(map(int, f.readline().rstrip().split()))

        ans = maximumToys(arr, r)

        print(str(ans) + '\n')

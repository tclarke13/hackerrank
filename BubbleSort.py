def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def countSwaps(a):
    l = len(a)
    swaps = 0
    for i in range(l):
        for j in range(l - 1):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)
                swaps += 1
    return swaps

if __name__ == '__main__':
    infile = "Input//Test.txt"
    with open(infile, 'r') as f:
        n = int(f.readline())

        a = list(map(int, f.readline().rstrip().split()))

        swaps = countSwaps(a)

        print("Array is sorted in {} swaps.".format(swaps))
        print("First Element: {}".format(a[0]))
        print("Last Element: {}".format(a[-1]))
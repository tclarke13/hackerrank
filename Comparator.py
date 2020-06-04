

if __name__ == '__main__':

    infile = "Input//Test.txt"
    with open(infile, 'r') as f:
        nr = f.readline().rstrip().split()

        n = int(nr[0])

        r = int(nr[1])

        arr = list(map(int, f.readline().rstrip().split()))

        ans = maximumToys(arr, r)

        print(str(ans) + '\n')

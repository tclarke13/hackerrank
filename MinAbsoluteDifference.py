def minimumAbsoluteDifference(arr):

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline().rstrip())

        arr = list(map(int, f.readline().rstrip().split()))

        result = minimumAbsoluteDifference(arr)

        print(str(result) + "\n")

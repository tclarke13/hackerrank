

def minimumAbsoluteDifference(arr):
    arr.sort()
    smallestDiff = abs(arr[1] - arr[0])
    for i in range(2, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if diff < smallestDiff:
            smallestDiff = diff

    return smallestDiff

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline().rstrip())

        arr = list(map(int, f.readline().rstrip().split()))

        result = minimumAbsoluteDifference(arr)

        print(str(result) + "\n")

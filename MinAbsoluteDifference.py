

def minimumAbsoluteDifference(arr):
    smallestDiff = abs(arr[0] - arr[1])
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff < smallestDiff:
                smallestDiff = diff

    return smallestDiff

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline().rstrip())

        arr = list(map(int, f.readline().rstrip().split()))

        result = minimumAbsoluteDifference(arr)

        print(str(result) + "\n")

def maxMin(arr, k):
    arr.sort()
    min_unfairness = arr[k - 1] - arr[0]
    for i in range(1, len(arr) - k + 1):
        val = arr[i + k - 1] - arr[i]
        if val < min_unfairness:
            min_unfairness = val

    return min_unfairness


if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline().rstrip())

        k = int(f.readline().rstrip())

        arr = []

        for _ in range(n):
            arr_item = int(f.readline().rstrip())
            arr.append(arr_item)

        result = maxMin(arr, k)

        print(str(result) + "\n")

def substrCount(n, s):
    counts = []
    letter = s[0]
    letterCount = 1
    for i in range(1, n):
        if s[i] != letter:
            counts.append([letter, letterCount])
            letterCount = 0
        letterCount += 1
        letter = s[i]
    counts.append([letter, letterCount])

    totalCount = 0

    for count in counts:
        totalCount += int(count[1] * (count[1] + 1) / 2)

    for i in range(1, len(counts) - 1):
        middle = counts[i]
        left = counts[i - 1]
        right = counts[i + 1]
        if middle[1] == 1 and left[0] == right[0]:
            totalCount += min(left[1], right[1])

    return totalCount




if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline())

        s = f.readline()

        result = substrCount(n, s)

        print(str(result) + "\n")

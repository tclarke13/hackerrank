from collections import defaultdict

def isValid(s):
    if len(s) == 0:
        return True

    letter_count = defaultdict(int)
    for letter in s:
        letter_count[letter] += 1

    letter_count = list(letter_count.values())

    one_freq = letter_count.count(1)
    max_count = max(letter_count)
    max_freq = letter_count.count(max_count)
    main_freq = 0
    main_count = letter_count[0]
    for i in letter_count:
        freq = letter_count.count(i)
        if freq > main_freq:
            main_freq = freq
            main_count = i
    outlier_freq = sum(1 for i in letter_count if i not in [1, main_count, max_count])

    print(one_freq)
    print(max_count)
    print(max_freq)
    print(main_count)
    print(main_freq)
    print(outlier_freq)

    if one_freq >= 2:
        if (max_count == 2 and max_freq == 1) or max_count == 1:
            return True
        else:
            return False
    elif one_freq == 1:
        if len(letter_count) == 1 or main_freq == len(letter_count) - 1:
            return True
        else:
            return False
    else:
        if (main_count == max_count and outlier_freq == 0) or (max_count == main_count + 1 and max_freq == 1):
            return True
        else:
            return False

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        s = f.readline()

        result = "YES" if isValid(s) else "NO"

        print(str(result) + "\n")

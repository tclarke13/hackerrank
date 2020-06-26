def find_substrings(S, D):
    dict = set()
    for word in D:
        dict.add(word)

    return find_substrings_recursive(S, dict)

def find_substrings_recursive(S, dict):
    if len(S) == 1:
        if S in dict:
            return [S]
        else:
            return []
    else:
        result = []
        if S in dict:
            result.append(S)
        for i in range(1, len(S)):
            left = S[0:i]
            if left in dict:
                right_substrings = find_substrings_recursive(S[i:len(S)],dict)
                for r in right_substrings:
                   result.append(left + " " + r)
        return list(result)


if __name__ == '__main__':
    S = "abcd"
    D = ["a", "b", "bc", "cd", "d", "c", "abcd", "abc", "ab"]
    print(find_substrings(S,D))

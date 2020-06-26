def find_substrings(S, D):
    dict = set()
    for word in D:
        dict.add(word)

    return find_substrings_recursive(S, dict)

def find_substrings_recursive(S, dict):
    if len(S) == 1:
        if S in dict:
            return set(S)
        else:
            return set()
    else:
        result = set()
        if S in dict:
            result.add(S)
        for i in range(1, len(S)):
            left_substrings = find_substrings_recursive(S[0:i],dict)
            right_substrings = find_substrings_recursive(S[i:len(S)],dict)
            for l in left_substrings:
               for r in right_substrings:
                   result.add(l + " " + r)
        return list(result)


if __name__ == '__main__':
    S = "abcd"
    D = ["a", "b", "bc", "cd", "d", "c", "abcd", "abc", "ab"]
    print(find_substrings(S,D))

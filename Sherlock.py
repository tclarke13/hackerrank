def isValid(s):
    return True

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        s = f.readline()

        result = "YES" if isValid(s) else "NO"

        print(str(result) + "\n")

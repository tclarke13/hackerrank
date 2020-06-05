def substrCount(n, s):

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        n = int(f.readline())

        s = f.readline()

        result = substrCount(n, s)

        print(str(result) + "\n")

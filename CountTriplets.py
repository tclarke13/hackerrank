from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    dic = defaultdict(list)
    for i in range(len(arr)):
        v = arr[i]
        dic[v].append(i)
    count = 0
    for k in dic:
        if k * r in dic and k * r * r in dic:
            idx_left = 0
            idx_mid = 0
            idx_right = 0
            len_left = len(dic[k])
            len_mid = len(dic[k*r])
            len_right = len(dic[k*r*r])
            while idx_mid < len_mid:
                if idx_right < len_right and dic[k*r][idx_mid] >= dic[k*r*r][idx_right]:
                    idx_right += 1
                elif idx_mid < len_mid and dic[k][idx_left] >= dic[k*r][idx_mid]:
                    idx_mid += 1
                else:
                    while idx_left < len_left - 1 and dic[k][idx_left + 1] < dic[k*r][idx_mid]:
                        idx_left += 1
                    count += (idx_left + 1) * (len_right - idx_right)
                    idx_mid += 1
    return int(count)


if __name__ == '__main__':

    infile = "Input//Test.txt"
    with open(infile, 'r') as f:
        nr = f.readline().rstrip().split()

        n = int(nr[0])

        r = int(nr[1])

        arr = list(map(int, f.readline().rstrip().split()))

        ans = countTriplets(arr, r)

        print(str(ans) + '\n')

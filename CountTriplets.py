import math
import os
import random
import re
import sys
from collections import defaultdict
from math import factorial

# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr) < 3:
        return 0
    dic = defaultdict(list)
    for i in range(len(arr)):
        v = arr[i]
        dic[v].append(i)
    print(dic)
    count = 0
    if r == 1:
        for k in dic:
            l = len(dic[k])
            if l >= 3:
                count += factorial(l) / (factorial(l - 3) * factorial(3))
        return int(count)
    for k in dic:
        if k * r * r < 10**9 and k * r in dic and k * r * r in dic:
            idx_left = 0
            idx_mid = 0
            idx_right = 0
            len_left = len(dic[k])
            len_mid = len(dic[k*r])
            len_right = len(dic[k*r*r])
            #print(dic[k][idx_left])
            #print(dic[k*r][idx_mid])
            #print(dic[k*r*r][idx_right])
            while idx_left < len_left and idx_mid < len_mid and idx_right < len_right:
                if dic[k*r][idx_mid] >= dic[k*r*r][idx_right]:
                    idx_right += 1
                elif dic[k][idx_left] >= dic[k*r][idx_mid]:
                    idx_mid += 1
                else:
                    while idx_left < len_left - 1 and dic[k][idx_left] < dic[k*r][idx_mid]:
                        idx_left += 1
                    count += (idx_left + 1) * (len_right - idx_right)
                    idx_mid += 1
    return int(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
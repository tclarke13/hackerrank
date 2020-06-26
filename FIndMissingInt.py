def find_missing(A, K):
    if len(A) == 0:
        return K

    if len(A) == 1:
        return A[0] + K

    for i in range(1, len(A)):
        if A[i] - A[i-1] > K:
            return A[i-1] + K
        else:
            K -= A[i] - A[i-1] - 1

    return A[-1] + K



if __name__ == '__main__':
    A = [-3,-1,2,4,7,10,15]
    #[-2,0,1,3,5,6,8,9,11,12,13,14,16,17,...]
    for K in range(1,15):
        print(find_missing(A, K))

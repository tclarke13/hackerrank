def moveUp(arr, i):
    while i < len(arr) - 1 and arr[i] > arr[i + 1]:
        temp = arr[i + 1]
        arr[i + 1] = arr[i]
        arr[i] = temp
        i += 1

def moveDown(arr, i):
    while i > 1 and arr[i] < arr[i - 1]:
        temp = arr[i - 1]
        arr[i - 1] = arr[i]
        arr[i] = temp
        i -= 1

def moveUpOrDown(arr, i):
    if i == 0:
        moveUp(arr, i)
    elif i == len(arr) - 1:
        moveDown(arr, i)
    else:
        if arr[i] > arr[i + 1]:
            moveUp(arr, i)
        elif arr[i] < arr[i - 1]:
            moveDown(arr, i)

def removeAndInsertAndSort(arr, insertVal, removeVal):
    i = 0
    while i < len(arr):
        if arr[i] == removeVal:
            arr[i] = insertVal
            break
        i += 1
    moveUpOrDown(arr, i)


def activityNotifications(expenditure, d):
    if len(expenditure) < d + 1:
        return 0
    sortedTrail = sorted(expenditure[0:d])
    numNotifications = 0
    for i in range(d, len(expenditure)):
        if d % 2 == 0:
            median = (sortedTrail[d // 2] + sortedTrail[d // 2 - 1]) / 2.0
        else:
            median = sortedTrail[d // 2]
        #print(median)
        if expenditure[i] >= median * 2:
            numNotifications += 1
        print(numNotifications)
        removeAndInsertAndSort(sortedTrail, expenditure[i], expenditure[i - d])
    return numNotifications

if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        nd = f.readline().split()
        n = int(nd[0])

        d = int(nd[1])

        expenditure = list(map(int, f.readline().rstrip().split()))

        result = activityNotifications(expenditure, d)

        print(str(result) + "\n")

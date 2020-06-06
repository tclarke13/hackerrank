from collections import deque, defaultdict

def calc_median(counts, d):
    sorted_keys = sorted(counts.keys())
    total_sum = 0
    if d % 2: #odd
        midpoint = d // 2 + 1
        i = 0
        while total_sum < midpoint:
            total_sum += counts[sorted_keys[i]]
            i += 1
        median = sorted_keys[i - 1]
    else: #even
        midpoint = d // 2
        i = 0
        while total_sum < midpoint:
            total_sum += counts[sorted_keys[i]]
            i += 1
        if total_sum == midpoint:
            median = (sorted_keys[i - 1] + sorted_keys[i]) / 2.0
        else:
            median = sorted_keys[i - 1]

    return median



def activity_notifications(expenditure, d):
    median_list = deque()
    counts = defaultdict(int)
    for i in range(d):
        median_list.append(expenditure[i])
        counts[expenditure[i]] += 1

    num_notifications = 0

    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * calc_median(counts, d):
            num_notifications += 1

        if i != len(expenditure) - 1:
            left_elem = median_list.popleft()
            counts[left_elem] -= 1
            if counts[left_elem] == 0:
                del counts[left_elem]
            median_list.append(expenditure[i])
            counts[expenditure[i]] += 1

    return num_notifications


if __name__ == '__main__':
    with open("Input//Test.txt", "r") as f:
        nd = f.readline().split()
        n = int(nd[0])

        d = int(nd[1])

        expenditure = list(map(int, f.readline().rstrip().split()))

        result = activity_notifications(expenditure, d)

        print(str(result) + "\n")

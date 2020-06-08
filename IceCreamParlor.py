def whatFlavors(cost, money):
    cost = [[cost[i], i+1] for i in range(len(cost))]
    cost.sort(key = lambda i : i[0])
    idx_left = 0
    idx_right = len(cost) - 1

    current_cost = cost[idx_left][0] + cost[idx_right][0]
    while current_cost != money:
        if current_cost > money:
            idx_right -= 1
        else:
            idx_left += 1
        current_cost = cost[idx_left][0] + cost[idx_right][0]

    smaller_idx = min(cost[idx_left][1], cost[idx_right][1])
    larger_idx = max(cost[idx_left][1], cost[idx_right][1])
    print(str(smaller_idx) + " " + str(larger_idx))

if __name__ == '__main__':
    infile = "Input//Test.txt"
    with open(infile, 'r') as f:
        t = int(f.readline().rstrip())

        for t_itr in range(t):
            money = int(f.readline().rstrip())

            n = int(f.readline().rstrip())

            cost = list(map(int, f.readline().rstrip().split()))

            whatFlavors(cost, money)
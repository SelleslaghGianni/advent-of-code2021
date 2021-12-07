from collections import Counter
from operator import itemgetter

input_data = [int(x) for x in open("7.in").read().strip().split(",")]


def solve(inp, part2):
    solution = Counter()
    fuel = 0
    for i in range(len(inp)):
        for x in inp:
            temp = abs(i - x)
            # If you add this commented out part, it takes roughly 15-20s to run, so let's not do that
            # if temp < 0:
            #     temp *= -1
            # temp2 = 0
            # for j in range(1, temp + 1):
            #     temp2 += j
            if part2:
                temp = temp * (temp + 1) / 2
            fuel += temp
        solution[i] = fuel
        fuel = 0
    min_key, min_count = min(solution.items(), key=itemgetter(1))
    return str(int(min_count))


print("Part 1: " + solve(input_data, False))
print("Part 2: " + solve(input_data, True))

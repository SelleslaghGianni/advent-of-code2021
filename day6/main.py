from collections import Counter

input_data = [int(x) for x in open("6.in").read().strip().split(",")]


def solve(data, days):
    c = Counter(data)
    c[0] = 0
    c[6] = 0
    c[7] = 0
    c[8] = 0
    for _ in range(days):
        count = c[0]
        c[0] = c[1]
        c[1] = c[2]
        c[2] = c[3]
        c[3] = c[4]
        c[4] = c[5]
        c[5] = c[6]
        c[6] = c[7] + count
        c[7] = c[8]
        c[8] = count
    return str(c.total())


print("Part 1: " + solve(input_data, 80))
print("Part 2: " + solve(input_data, 256))


# My first solution, worked for part 1 but part 2 refuses :(
# for j in range(80):
#     count = 0
#     for i, c in enumerate(input_data):
#         if c == 0:
#             count += 1
#             input_data[i] = 6
#         else:
#             input_data[i] -= 1
#     for _ in range(count):
#         input_data.append(8)
#     print(j)

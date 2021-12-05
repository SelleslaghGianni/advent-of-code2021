input_data = [x for x in open("5.in").read().strip().split("\n")]
field_p1 = [[0 for _ in range(len(input_data) * 2)] for _ in range(len(input_data) * 2)]
field_p2 = [[0 for _ in range(len(input_data) * 2)] for _ in range(len(input_data) * 2)]
x1_arr = []
x2_arr = []
y1_arr = []
y2_arr = []

for i, line in enumerate(input_data):
    left, right = line.split("->")
    x1, y1 = left.split(",")
    x2, y2 = right.split(",")
    x1_arr.append(int(x1))
    x2_arr.append(int(x2))
    y1_arr.append(int(y1))
    y2_arr.append(int(y2))

for i in range(len(x1_arr)):
    if x1_arr[i] == x2_arr[i] or y1_arr[i] == y2_arr[i]:
        for x in range(min(x1_arr[i], x2_arr[i]), max(x1_arr[i], x2_arr[i]) + 1):
            for y in range(min(y1_arr[i], y2_arr[i]), max(y1_arr[i], y2_arr[i]) + 1):
                field_p1[x][y] += 1
                field_p2[x][y] += 1
    else:
        if x1_arr[i] < x2_arr[i]:
            for x in range(x1_arr[i], x2_arr[i] + 1):
                if y1_arr[i] < y2_arr[i]:
                    field_p2[x][x - x1_arr[i] + y1_arr[i]] += 1
                else:
                    field_p2[x][y1_arr[i] - (x - x1_arr[i])] += 1
        else:
            for x in range(x2_arr[i], x1_arr[i] + 1):
                if y1_arr[i] > y2_arr[i]:
                    field_p2[x][x - x2_arr[i] + y2_arr[i]] += 1
                else:
                    field_p2[x][y2_arr[i] - (x - x2_arr[i])] += 1

p1 = 0
for x in range(len(field_p1[0])):
    for y in range(len(field_p1[0])):
        if field_p1[x][y] > 1:
            p1 += 1
p2 = 0
for x in range(len(field_p2[0])):
    for y in range(len(field_p2[0])):
        if field_p2[x][y] > 1:
            p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))

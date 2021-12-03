input_data = [x for x in open("input.txt").read().strip().split("\n")]

output = {}
length = len(input_data[0])

for line in input_data:
    for i, char in enumerate(line):
        if char == "1":
            if str(i) not in output:
                output[str(i)] = 1
            else:
                output[str(i)] += 1


result = ""
for i in range(len(output)):
    if output[str(i)] > 500:
        result += "1"
    else:
        result += "0"

gamma = int(result, 2)
epsilon = int("".join("1" if x == "0" else "0" for x in result), 2)


oxygen = set(input_data)
for i in range(length):
    column = "".join(line[i] for line in oxygen)
    if column.count("0") <= column.count("1"):
        char = "1"
    else:
        char = "0"

    oxygen = oxygen - set(line for line in oxygen if line[i] == char)
    if len(oxygen) == 1:
        oxygen = int(max(oxygen), 2)
        break

co2 = set(input_data)
for i in range(length):
    column = "".join(line[i] for line in co2)
    if column.count("0") > column.count("1"):
        char = "1"
    else:
        char = "0"

    co2 = co2 - set(line for line in co2 if line[i] == char)
    if len(co2) == 1:
        co2 = int(max(co2), 2)
        break

print("Part 1: " + str(gamma * epsilon))
print("Part 2: " + str(oxygen * co2))

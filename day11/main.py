input_data = []
with open("11.in", "r") as f:
    for _ in range(10):
        input_data.append(f.readline().split("\n"))


field = []
for line in input_data:
    row = []
    for char in line:
        for num in char:
            if num == ",":
                field += row
                row = []
            row.append(int(num))
    field.append(row)
    row = []

flashes = 0
flashing = set()
not_synchronized = True
day = 0
while not_synchronized:
    if day == 100:
        print("Part 1: " + str(flashes))
    if len(flashing) == 100:
        print("Part 2: " + str(day))
        not_synchronized = False
    flashing = set()
    for j in range(100):
        for x in range(len(field)):
            for y in range(len(field[0])):
                if j == 0:
                    field[x][y] += 1
                if field[x][y] > 9:
                    if (x, y) not in flashing:
                        flashing.add((x, y))
                        flashes += 1
                        field[x][y] = 0
                        for xx in [-1, 0, 1]:
                            for yy in [-1, 0, 1]:
                                x_dir = x + xx
                                y_dir = y + yy
                                if (
                                    0 <= x_dir < len(field)
                                    and 0 <= y_dir < len(field[0])
                                    and (x, y) in flashing
                                    and (x_dir, y_dir) not in flashing
                                ):
                                    field[x_dir][y_dir] += 1
    day += 1

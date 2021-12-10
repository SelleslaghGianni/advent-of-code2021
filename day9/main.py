input_data = []
with open("9.in", "r") as f:
    for _ in range(100):
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

direction_x = [-1, 0, 1, 0]
direction_y = [0, 1, 0, -1]
risk_levels = 0
for x in range(len(field)):
    for y in range(len(field[0])):
        low_point = True
        for direction in range(4):
            x_dir = x + direction_x[direction]
            y_dir = y + direction_y[direction]
            if (
                0 <= x_dir < len(field)
                and 0 <= y_dir < len(field[0])
                and field[x_dir][y_dir] <= field[x][y]
            ):
                low_point = False
        if low_point:
            risk_levels += field[x][y] + 1


# Pseudocode for BFS from: https://favtutor.com/blogs/breadth-first-search-python.
# Using an array for visited members was very slow, changed into a set to speed things up.
basin = []
visited = set()
for x in range(len(field)):
    for y in range(len(field[0])):
        if (x, y) not in visited and field[x][y] != 9:
            size = 0
            queue = []
            queue.append((x, y))
            while queue:
                (x, y) = queue.pop(0)
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                size += 1
                for direction in range(4):
                    x_dir = x + direction_x[direction]
                    y_dir = y + direction_y[direction]
                    if (
                        0 <= x_dir < len(field)
                        and 0 <= y_dir < len(field[0])
                        and field[x_dir][y_dir] != 9
                    ):
                        queue.append((x_dir, y_dir))
            basin.append(size)

basin.sort()
basin_len = len(basin)
size_largest_basins = basin[basin_len - 3] * basin[basin_len - 2] * basin[basin_len - 1]
print("Part 1: " + str(risk_levels))
print("Part 2: " + str(size_largest_basins))

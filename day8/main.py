import itertools

sequences = []
with open("8.in", "r") as f:
    for line in f:
        sequences.append(line.split())

digit_map = {
    "acedgfb": 8,
    "cdfbe": 5,
    "gcdfa": 2,
    "fbcad": 3,
    "dab": 7,
    "cefabd": 9,
    "cdfgeb": 6,
    "eafb": 4,
    "cagedb": 0,
    "ab": 1,
}
digit_map = {"".join(sorted(key)): value for key, value in digit_map.items()}


p1 = 0
for line in sequences:
    output_value = [line[x] for x in range(11, 15)]
    for num in output_value:
        if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
            p1 += 1

# Pseudocode from reddit: for every permutation of A to G, test to see if all translated
# strings are compatible with the digit formations, if they all are, use that permutation
# to translate the second set of strings.
p2 = 0
for line in sequences:
    signal_pattern = [line[x] for x in range(10)]
    output_value = [line[x] for x in range(11, 15)]
    for perm in itertools.permutations("abcdefg"):
        perm_map = {key: value for key, value in zip(perm, "abcdefg")}

        signal_pattern_list = ["".join(perm_map[c] for c in x) for x in signal_pattern]
        output_value_list = ["".join(perm_map[c] for c in x) for x in output_value]

        if all("".join(sorted(ans)) in digit_map for ans in signal_pattern_list):
            output_value_list = ["".join(sorted(x)) for x in output_value_list]
            p2 += int("".join(str(digit_map[x]) for x in output_value_list))
            break

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))

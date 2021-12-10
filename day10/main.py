from collections import deque

input_data = [x.split("\n")[0] for x in open("10.in").readlines()]

p1 = 0
p2 = []
for line in input_data:
    stack = deque()
    corrupted = False
    for char in line:
        match char:
            case '(':
                stack.append(char)
            case '[':
                stack.append(char)
            case '{':
                stack.append(char)
            case '<':
                stack.append(char)
            case ')':
                temp = stack.pop()
                if temp == '(':
                    continue
                else:
                    corrupted = True
                    p1 += 3
            case ']':
                temp = stack.pop()
                if temp == '[':
                    continue
                else:
                    corrupted = True
                    p1 += 57
            case '}':
                temp = stack.pop()
                if temp == '{':
                    continue
                else:
                    corrupted = True
                    p1 += 1197
            case '>':
                temp = stack.pop()
                if temp == '<':
                    continue
                else:
                    corrupted = True
                    p1 += 25137
    if not corrupted:
        stack.reverse()
        temp_p2 = 0
        for symbol in stack:
            match symbol:
                case '(':
                    temp_p2 = temp_p2 * 5 + 1
                case '[':
                    temp_p2 = temp_p2 * 5 + 2
                case '{':
                    temp_p2 = temp_p2 * 5 + 3
                case '<':
                    temp_p2 = temp_p2 * 5 + 4
        p2.append(temp_p2)

print("Part 1: " + str(p1))

p2.sort()
print("Part 2: " + str(p2[len(p2)//2]))

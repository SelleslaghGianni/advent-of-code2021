input_data = open('input.txt').read().splitlines()

counter_p1 = 0
counter_p2 = 0
for i in range(len(input_data)):
    previous = int(input_data[i-1])
    current = int(input_data[i])
    if previous < current:
        counter_p1 += 1
    A = int(input_data[i-3]) + int(input_data[i-2]) + int(input_data[i-1])
    B = int(input_data[i-2]) + int(input_data[i-1]) + int(input_data[i])
    if A < B:
        counter_p2 += 1

print("p1: " + str(counter_p1))
print("p2: " + str(counter_p2))

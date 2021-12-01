input_data = open('input.txt').read().splitlines()

counter_p1 = 0
counter_p2 = 0
for i in range(len(input_data)):
    previous = int(input_data[i-1])
    current = int(input_data[i])
    if previous < current:
        counter_p1 += 1
    previous_p2 = int(input_data[i-3])
    current_p2 = int(input_data[i])
    if previous_p2 < current_p2:
        counter_p2 += 1

print("p1: " + str(counter_p1))
print("p2: " + str(counter_p2))

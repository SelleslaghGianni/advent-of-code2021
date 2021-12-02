inp = [str(x).split('\n') for x in open('input.txt')]
proc_inp = []
for line in inp:
    proc_inp.append(line[0])

data_p1 = {'horizontal': 0, 'depth': 0}
data_p2 = {'horizontal': 0, 'depth': 0, 'aim': 0}

for instr in proc_inp:
    inst, amt = instr.split(' ')
    if inst == 'down':
        data_p1['depth'] += int(amt)
        data_p2['aim'] += int(amt)
    if inst == 'up':
        data_p1['depth'] -= int(amt)
        data_p2['aim'] -= int(amt)
    if inst == 'forward':
        data_p1['horizontal'] += int(amt)
        data_p2['horizontal'] += int(amt)
        data_p2['depth'] += data_p2['aim'] * int(amt)
print(data_p1['horizontal']*data_p1['depth'])
print(data_p2['horizontal']*data_p2['depth'])

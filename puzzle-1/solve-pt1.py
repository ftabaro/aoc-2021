with open("input.txt") as fin:
    lines = fin.readlines()

inc=0
dec=0
for i in range(1, len(lines)): 

    prev = int(lines[i - 1])
    cur = int(lines[i])

    if cur > prev:
        inc += 1
    else:
        dec += 1
print(inc)

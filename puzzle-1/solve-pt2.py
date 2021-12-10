def calc_window(w):
    w = [int(x) for x in w]
    return sum(w)

with open("input.txt") as fin:
    lines = fin.readlines()

inc=0
dec=0
for i in range(1, len(lines) - 1): 

    cur = calc_window(lines[i - 1: i + 2])
    nex = calc_window(lines[i : i + 3])
    
    if nex > cur:
        inc += 1
    else:
        dec += 1

print(inc, dec)

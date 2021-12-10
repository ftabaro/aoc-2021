with open("input.txt") as fin:
    lines = fin.readlines()

hor = 0
dep = 0
for line in lines:
    instr,amount = line.strip().split()
    amount = int(amount)
    if instr == "forward":
        hor += amount
    elif instr == "down":
        dep += amount
    elif instr == "up":
        dep -= amount

print(hor * dep)

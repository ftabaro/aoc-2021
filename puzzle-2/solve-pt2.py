with open("input.txt") as fin:
    lines = fin.readlines()

hor = 0
dep = 0
aim = 0
for line in lines:
    instr,amount = line.strip().split()
    amount = int(amount)
    if instr == "forward":
        hor += amount
        dep += aim * amount
    elif instr == "down":
        aim += amount
    elif instr == "up":
        aim -= amount

print(hor * dep)

import sys

counts = [[0,0]]
with open("input.txt") as fin:
	for line in fin:
		line = line.rstrip()
		for i in range(len(line)):
			char = int(line[i])
			if len(counts) < i + 1:
				counts.append([0,0])
			counts[i][char] += 1

def get_rate(f):
	l = [f(range(len(values)), key=values.__getitem__) for values in counts]
	l = [str(x) for x in l]
	l = ''.join(l)
	print(l)
	l = int(l, 2)
	return l

gamma_rate = get_rate(max) 
epsilon_rate = get_rate(min)

power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
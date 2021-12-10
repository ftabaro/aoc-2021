ndays = 257 # for part 1 set this to 181
nstates = 9 # zero is a state

fishes = [[0] * nstates ] * ndays

with open("input.txt") as fin:
	init = [ int(x) for x in fin.readline().strip().split(",")]
	states = [0] * nstates
	for i in range(nstates):
		states[i] = init.count(i)
	
fishes[0] = states
for i in range(1, ndays):
	newborn = fishes[i - 1][0]
	for j in range(nstates - 1):
		if j == 6:
			fishes[i][6] = fishes[i - 1][j + 1] + newborn
		else:
			fishes[i][j] = fishes[i - 1][j + 1]
	fishes[i][-1] = newborn

last = fishes[-1]
print(sum(last))

with open("input.txt") as fin:
	starting_pos = [ int(x) for x in fin.readline().strip().split(",") ] 

out = []
for p in range(max(starting_pos)):
	costs = []
	for pos in starting_pos:
		cost = abs(pos - p)
		costs.append(cost)
	total_cost = sum(costs)

	out.append([p, total_cost])

print(sorted(out, key = lambda x: x[1]))

cheapest = min(out, key = lambda x: x[1])
print(cheapest)
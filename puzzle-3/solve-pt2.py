def filter_lines(lines, sele_fun, j = 0):
	if len(lines) == 1:
		return lines[0]
	chars = [line[j] for line in lines]
	counts = [chars.count("0"), chars.count("1")]
	k = sele_fun(counts)
	out = [line for line in lines if line[j] == k]
	return filter_lines(out, sele_fun, j + 1)


def find_oxigen_generator_rating(lines):
	def sele_fun(counts):
		k = str(max(range(len(counts)), key=counts.__getitem__))
		if counts[0] == counts[1]:
			k = "1"
		return k
	res = filter_lines(lines, sele_fun)
	return(int(res, 2))


def find_co2_scrubber_rating(lines):
	def sele_fun(counts):
		k = str(min(range(len(counts)), key=counts.__getitem__))
		if counts[0] == counts[1]:
			k = "0"
		return k
	res = filter_lines(lines, sele_fun)
	return(int(res, 2))


def main():
	with open("input.txt") as fin:
		lines = fin.readlines()
		lines = [line.rstrip() for line in lines]

	oxigen_generator_rating = find_oxigen_generator_rating(lines)
	co2_scrubber_rating = find_co2_scrubber_rating(lines)

	print(oxigen_generator_rating * co2_scrubber_rating)


if __name__ == '__main__':
	main()
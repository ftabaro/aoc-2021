with open("input.txt") as fin:
	draws = [int(x) for x in fin.readline().rstrip().split(",")]
	# [
	#   (board, x, y, value, markd), 
	#   (board, x, y, value, markd),
	#   ...
	# ]
	boards = []
	bi = None
	for line in fin:
		line = line.rstrip()
		if line != "":
			ri += 1
			board_line = line.split()
			for ci in range(len(board_line)):
				boards.append([bi, ri, ci, int(board_line[ci]), False])
		else:
			bi = bi + 1 if not bi is None else 0
			ri = 0


def find_bingo(boards):
	for cell in filter(lambda x: x[4], boards):
		bi, ri, ci = cell[0], cell[1], cell[2]
		row = filter(lambda x: x[0] == bi and x[1] == ri, boards)
		col = filter(lambda x: x[0] == bi and x[2] == ci, boards)
		is_bingo = all(map(lambda x: x[4], row)) or all(map(lambda x: x[4], col))
		if is_bingo:
			return True, bi
	return False, None


def calc_score(board):
	unmarkd = filter(lambda x: not x[4], board)
	scores = map(lambda x: x[3], unmarkd)
	return sum(scores)


for draw in draws:
	for cell in filter(lambda x: x[3] == draw, boards):
		cell[4] = True
	is_bingo, bi = find_bingo(boards)
	if is_bingo:
		bingo_board = filter(lambda x: x[0] == bi, boards)
		score = calc_score(bingo_board)
		print(score * draw)
		break


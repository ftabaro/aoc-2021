with open("input.txt") as fin:
	draws = [int(x) for x in fin.readline().rstrip().split(",")]
	# boards = [
	#   (board, x, y, value, markd), 
	#   (board, x, y, value, markd),
	#   ...
	# ]
	boards = []
	bi = None
	for line in fin:
		line = line.rstrip()
		if line != "":
			board_line = line.split()
			for ci in range(len(board_line)):
				boards.append([bi, ri, ci, int(board_line[ci]), False])
			ri += 1
		else:
			bi = bi + 1 if not bi is None else 0
			ri = 0


def find_bingo(boards):
	bingos = []
	for cell in filter(lambda x: x[4], boards):		
		bi, ri, ci, _, _ = cell
		row = filter(lambda x: x[0] == bi and x[1] == ri, boards)
		col = filter(lambda x: x[0] == bi and x[2] == ci, boards)
		is_bingo = all(map(lambda x: x[4], row)) or all(map(lambda x: x[4], col))
		if is_bingo:
			bingos.append(bi)
	return set(bingos)


def calc_score(board):
	unmarkd = filter(lambda x: not x[4], board)
	scores = map(lambda x: x[3], unmarkd)
	return sum(scores)

winning_boards = []
has_won = []
from pprint import pprint as pp
for draw in draws:
	print(f"Drawing {draw}...")
	for cell in filter(lambda x: x[3] == draw, boards):
		cell[4] = True
	bingos = find_bingo(boards)
	if len(bingos) > 0:
		for bi in bingos:
			bingo_board = filter(lambda x: x[0] == bi, boards)
			score = calc_score(bingo_board)
		
			final_score = score * draw
			winning_boards.append((bi, draw, score, final_score))

			print(f"Board {bi} BINGO! - final score: {final_score}")
			pp([x for x in filter(lambda x: x[0] == bi, boards)])
			boards = list(filter(lambda x: x[0] != bi, boards))


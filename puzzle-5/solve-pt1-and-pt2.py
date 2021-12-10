from pprint import pprint as pp

class Vent:
	def __init__(self, x0, y0, x1, y1):
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1

		self.is_horizontal = self.y0 == self.y1
		self.is_vertical = self.x0 == self.x1

		self.a = abs(x0 - x1)
		self.b = abs(y0 - y1)

	@staticmethod
	def find_mixmax(a,b):
		return min(a,b), max(a,b)
	
	def get_coords(self):
		if self.is_vertical:
			y = min(self.y0, self.y1)
			for p in range(self.b + 1):
				yield (self.x0, y + p)

		elif self.is_horizontal:
			x = min(self.x0, self.x1)
			for p in range(self.a + 1):
				yield (x + p, self.y0)

		else:
			xmin, xmax = Vent.find_mixmax(self.x0, self.x1)
			ymin, ymax = Vent.find_mixmax(self.y0, self.y1)

			if xmin == self.x0:
				x = range(self.x0, self.x1 + 1)
				if self.y0 > self.y1:
					y = range(self.y0, self.y1 - 1, -1)
				else:
					y = range(self.y0, self.y1 + 1)
			else:
				x = range(self.x1, self.x0 + 1)
				if self.y1 > self.y0:
					y = range(self.y1, self.y0 - 1, -1)
				else:
					y = range(self.y1, self.y0 + 1)


			for i,j in zip(x, y):
				yield (i, j)

with open("input.txt") as fin:
	vents = {}
	for line in fin:

		line = line.rstrip().split("->")
		x0, y0 = [int(x) for x in line[0].strip().split(",")]
		x1, y1 = [int(x) for x in line[1].strip().split(",")]
		vent = Vent(x0, y0, x1, y1)

		for pos in vent.get_coords():
			if pos not in vents:
				vents[pos] = 0
			vents[pos] += 1

print(len(list(filter(lambda x: x > 1, vents.values()))))
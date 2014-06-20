def my_max(a, b):
	"Definit le max(int, list) et max(list, list)"
	if type(a) == list:
		a = max(a)
	if type(b) == list:
		b = max(b)
	return max(a, b)

def el_to_list(el):
	return map(int, el.split('-'))

def matrix_from_txt(s):
	l = s.split('\n')[:-1]
	l = map(el_to_list, l)
	matrix_length = reduce(my_max, l) + 1
	matrix = [[0 for i in xrange(matrix_length)] for j in xrange(matrix_length)]
	for i, j in l:
		matrix[i][j] = 1
		matrix[j][i] = 1
	return matrix

class AdjacencyMatrix:
	def __init__(self, matrix):
		self.matrix = matrix
		self.n = len(matrix)
	
	def get_neighbours(self, node):
		"Returns the neighbours of a node"

		return [i for i in xrange(self.n) if matrix[i][node] == 1]

	def get_neighbours(matrix, node):
		neighbours = []
		for i in xrange(len(matrix)):
			if matrix[i][node] == 1:
				neighbours.append(i)
		return neighbours

def shortest_path(start, end, matrix):
	colored_nodes = set([])
	queue = []
	queue.insert(0, [start])
	while len(queue) != 0:
		path = queue.pop(0)
		node = path[-1]
		colored_nodes.add(node)
		if (node == end):
			return path
		neighbours = get_neighbours(matrix, node)
		for neighbour in neighbours:
			if neighbour not in colored_nodes:
				queue.append(path + [neighbour])

if __name__ == "__main__":
	f = open("nodes.txt", "r")
	matrix = matrix_from_txt(f.read())
	bfs(1, 0, matrix)

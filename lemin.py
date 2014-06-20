import copy
import runningMouse

def my_max(a, b):
	"Defines the max between two lists and between a list and a scalar"

	if type(a) == list:
		a = max(a)
	if type(b) == list:
		b = max(b)
	return max(a, b)

class AdjacencyMatrix:
	def __init__(self, matrix):
		self.matrix = matrix
		self.n = len(matrix)
	
	def __str__(self):
		return str(self.matrix)

	@classmethod
	def from_string(cls, s):
		"Creates an adjency matrix from a string"

		# Split by lines
		l = s.split('\n')[:-1]

		# Transform ["1-2", "2-3"] to [(1,2), (2,3)]
		l = [map(int, el.split('-')) for el in l]

		matrix_length = reduce(my_max, l) + 1
		matrix = [[0 for i in xrange(matrix_length)] for j in xrange(matrix_length)]
		for i, j in l:
			matrix[i][j] = 1
			matrix[j][i] = 1
		return cls(matrix)
	
	def get_neighbours(self, node):
		"Returns the neighbours of a node"

		return [i for i in xrange(self.n) if self.matrix[i][node] == 1]

	def shortest_path(self, start, end):
		"Returns the shortest path between two nodes using the BFS algorithm"

		visited_nodes = set([])
		queue = [[start]]
		while len(queue) > 0:
			path = queue.pop(0)
			node = path[-1]
			if (node == end):
				return path
			visited_nodes.add(node)
			neighbours = self.get_neighbours(node)
			queue += [path + [neighbour] for neighbour in neighbours if neighbour not in visited_nodes]
		return None
	
	def remove_node_edges(self, node):
		"Removes the edges from a node"

		for i in xrange(self.n):
			self.matrix[i][node] = 0
			self.matrix[node][i] = 0
	
	def remove_nodes_edges(self, nodes):
		"Removes the edges from a list of nodes"

		map(self.remove_node_edges, nodes)

if __name__ == "__main__":
	mult_paths = []
	f = open("nodes.txt", "r")
	matrix = AdjacencyMatrix.from_string(f.read())
	path =  matrix.shortest_path(0,1)
	mult_paths.append(path)
	while path:
		matrix.remove_nodes_edges(path[1:-1])
		path = matrix.shortest_path(0,1)
		if path:
			mult_paths.append(path)
	print mult_paths
	

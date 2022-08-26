# Directed Weighted Graph representation using nested dictionaries

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {'D': 2, 'E': 7, 'F': 3},
    'C': {'G': 3},
    'D': {},
    'E': {},
    'F': {'H': 6},
    'G': {'I': 5},
    'H': {},
    'I': {}
}

# Using Nodes:

class AdjNode:
	def __init__(self, data):
		self.vertex = data
		self.next = None

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V

	# Function to add an edge in an undirected graph
	def add_edge(self, src, dest):
		# Adding the node to the source node
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		# Adding the source node to the destination as
		# it is the undirected graph
		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
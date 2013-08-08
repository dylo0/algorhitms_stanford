
def build_weighted_graph(filename):
    """
    Reads file and creates weighted graph:
    	keys - verticies
		values - list of lists: [[other_vertex, weight], [...], ...]
    """
    f = open(filename, "r")
    graph = {}
    
    for line in f:
    	vertex = line.split()
        graph[int(vertex[0])] = {int(v.split(',')[0]): int(v.split(',')[1]) for v in vertex[1:]}
    
    return graph


def shortest_path(graph, vertex_A, vertex_B):
	"""
	My implementation of Dijkstra's shortest-path algorithm
	Input:
		verticies A and B
		graph - weighted dictionary represented graph:
			keys - verticies
			values - list of lists: [[other_vertex, weight], [...], ...]
	
	Returns weighted shortest distance between A and B
	"""
	assert vertex_A in graph
	assert vertex_B in graph

	X = [vertex_A]
	distances = {vertex_A: 0}

	while vertex_B not in X:
		temp = []
		for vertex in X:
			for other in graph[vertex]:
				if other not in X:
					distance = distances[vertex] + graph[vertex][other]
					temp.append((distance, other))

		d_greedy = min(temp)
		X.append(d_greedy[1])
		distances[d_greedy[1]] = d_greedy[0]

	return distances[vertex_B]


graph =  build_weighted_graph('dijkstraData.txt')
others = [7,37,59,82,99,115,133,165,188,197]

print [shortest_path(graph, 1, other) for other in others]

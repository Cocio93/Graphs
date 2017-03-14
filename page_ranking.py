import collections

def print_scores():
	for node in collections.OrderedDict(sorted(graph.items())):
		print(node, ":", "{0:.4f}".format(graph_scores[node]))

def page_rank(node, d=0.85):
	n = len(graph)
	d =  0.85
	sum_nodes = sum(map(lambda x: graph_scores[x] / len(graph[x]), graph[node]))

	return ((1-d) / n) + (d*sum_nodes)

def page_rank_graph(graph, no_of_its=100):
		for _ in range(no_of_its):
			for node in graph:
				graph_scores[node] = page_rank(node)

graph = {'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C'],
		'G': ['A','B','C','D','E','F']}

graph_scores = {'A': 1,
				'B': 1,
				'C': 1,
				'D': 1,
				'E': 1,
				'F': 1,
				'G': 1}

page_rank_graph(graph)
print_scores()

## Cheapest or Most Expensive path in graph

def path_cost(p):
	path_sum = 0
	for node in p:
		path_sum += graph_scores[node]
	return path_sum

def find_path(graph, start, end, path=[], max=False):
	path = path + [start]
	if start == end:
		return path
	if not graph[start]:
		return None
	best_path = None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path, max)
			if newpath:
				if max:
					if not best_path or path_cost(newpath) > path_cost(best_path):
						best_path = newpath
				if not max:
					if not best_path or path_cost(newpath) < path_cost(best_path):
						best_path = newpath
	return best_path

path = find_path(graph, 'A', 'D')
print(path, "Cost:", path_cost(path))

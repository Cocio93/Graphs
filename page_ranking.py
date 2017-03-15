import collections
import numpy as np
student_graph = {'Adam' : ['Phillip', 'Carol'],
				'Jonnas' : ['Adam', 'Carol'],
				'Carol' : ['Jonnas', 'Adam', 'Laura', 'Jack'],
				'Jack' : ['Lily', 'Peter', 'Jacob', 'Emil', 'Mathias', 'Carol'],
				'Lily' : ['Jack'],
				'Peter' : ['Jack'],
				'Emil' : ['Jack'],
				'Mathias' : ['Jack', 'Jacob'],
				'Jacob' : ['Jack', 'Mathias', 'Mikkel', 'Emma', 'Laura'],
				'Mikkel' : ['Jacob', 'Mark'],
				'Laura' : ['Carol', 'Jacob', 'Emma'],
				'Emma' : ['Jacob', 'Laura'],
				'Phillip' : ['Adam', 'Mark'],
				'Mark' : ['Phillip', 'Mikkel']}

graph_scores = {}
for key in student_graph:
	graph_scores.update({ key : 1})

def print_scores():
	for node in collections.OrderedDict(sorted(student_graph.items())):
		print(node, ":", "{0:.4f}".format(graph_scores[node]))

def page_rank(node, d=0.85):
	n = len(student_graph)
	d =  0.85
	sum_nodes = sum(map(lambda x: graph_scores[x] / len(student_graph[x]), student_graph[node]))

	return ((1-d) / n) + (d*sum_nodes)

def page_rank_graph(graph, no_of_its=100):
		for _ in range(no_of_its):
			for node in student_graph:
				graph_scores[node] = page_rank(node)

page_rank_graph(student_graph)
print_scores()




## Cheapest or Most Expensive path in graph

def path_cost(p):
	path_sum = 0
	for node in p:
		path_sum += graph_scores[node]
	return path_sum

def find_path(graph, start, end, path=[], max=True):
	path = path + [start] ## Converting start to list, in order to append to path
	if start == end:
		return path
	if not graph[start]: ## If Graph doesnt contain node
		return None
	best_path = None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path, max)
			if newpath:
				if max == True:
					if not best_path or path_cost(newpath) > path_cost(best_path):
						best_path = newpath
				if max == False:
					if not best_path or path_cost(newpath) < path_cost(best_path):
						best_path = newpath
				if max == None:
					if not best_path or len(newpath) < len(best_path):
						best_path = newpath
	return best_path

path = find_path(student_graph, 'Emil', 'Adam')
print(path)

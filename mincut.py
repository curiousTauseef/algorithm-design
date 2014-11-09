import random
import copy

def subroutine(graph):
    while (len(graph) > 2):
        node1 = random.choice(list(graph))
        node2 = random.choice(graph[node1])
        graph[node1] = [x for x in graph[node1] + graph[node2] if x not in (node1, node2)]
        del graph[node2]
        for node in graph:
            graph[node] = [x if x != node2 else node1 for x in graph[node]]
        values = list(graph.values)
    return len(values[0])

def readgraph(file):
    graph = {}
    with open (file) as f:
        for line in f:
            line = [int(x) for x in line.split()]
            graph[line.pop(0)] = line
    return graph
        
def mincut(n, file):
    graph = readgraph(file)
    cut = float("inf")
    for i in range (n):
        cut = min(cut, subroutine(copy.deepcopy(graph)))
    return cut

print (mincut(10, 'mincut.txt'))


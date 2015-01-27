import random
import copy
import itertools

def subroutine(graph):
    while (len(graph) > 2):
        id1 = random.choice(list(graph.keys()))
        id2 = random.choice(graph[id1])
        contracted = graph[id1] + graph[id2]
        del graph[id2]
        graph[id1] = [x for x in contracted if x not in (id1, id2)]
        for node in graph:
            graph[node] = [id1 if x == id2 else x for x in graph[node]]
        values = list(graph.values())
    return len(values[0])

def readgraph(file):
    graph = {}
    with open (file) as f:
        for line in f:
            line = [int(x) for x in line.split()]
            graph[line.pop(0)] = line
    return graph
        
def mincut(n, graph):
    cut = float("inf")
    for i in range (n):
        cut = min(cut, subroutine(copy.deepcopy(graph)))
    return cut

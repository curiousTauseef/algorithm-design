import numpy as np
import math

def bellmanford(graph, source):

    n = graph.get_num_vertices()
    dist = np.full(n, np.inf)
    dist[source] = 0
    pred = np.full(n, np.nan)
    for i in range(n):
        for u in range(n):
            for v in graph.get_children(u):
                newdist = dist[u] + graph.get_dist(u,v)
                if (newdist < dist[v]):
                    dist[v] = newdist
                    pred[v] = u
    for u in range(n):
        for v in graph.get_children(u):
            newdist = dist[u] + graph.get_dist(u,v)
            assert dist[v] <= newdist, "Negative weight cycle!"
    return (dist, pred)

def getpath(pred, i):
    if math.isnan(i):
        return []
    else:
        return getpath(pred, pred[int(i)]) + [int(i)]

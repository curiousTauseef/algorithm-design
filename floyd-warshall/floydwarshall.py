import numpy as np

def floydwarshall(graph):
    n = graph.get_num_vertices()
    dist = np.full((n, n), np.inf)
    pred = np.full((n, n), -1).astype(int)
    np.fill_diagonal(dist, 0)
    for u in range(n):
        for v in graph.get_children(u):
            dist[u, v] = graph.get_dist(u, v)
            pred[u, v] = u
    for k in range(n):
        newdist = dist[np.newaxis, k, :] + dist[:, k, np.newaxis]
        ind = np.where(newdist < dist)
        dist[ind] = newdist[ind]
        pred[ind] = pred[k, ind[1]]
    return (dist, pred)

def getpath(pred, i, j):
    if i == j:
        return [i]
    else:
        return getpath(pred, i, pred[i, j]) + [j]

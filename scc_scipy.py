from scipy.sparse import coo_matrix, csgraph
import numpy as np

def compute_scc(file, n):
    with open(file) as f:
        graph = np.array([list(map(int, line.split())) for line in f])
        xs, ys = graph[:, 0], graph[:, 1]
        data = np.ones(len(graph))
        adj_matrix = coo_matrix((data, (xs, ys)), shape = (n, n))
        return csgraph.connected_components(adj_matrix, connection = 'strong')

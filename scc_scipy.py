from scipy.sparse import coo_matrix, csgraph
import numpy as np

def compute_scc(file, number_of_nodes):
    with open(file) as f:
        data = np.array([list(map(int, line.split())) for line in f])
        adj_matrix = coo_matrix((np.ones(len(data)), (data[:, 0], data[:, 1])), shape = (number_of_nodes, number_of_nodes))
        return csgraph.connected_components(adj_matrix, connection = 'strong')

compute_scc('graf', 875715)

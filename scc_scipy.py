# from scipy.sparse import coo_matrix as matrix
# from scipy.sparse.csgraph import connected_components
import numpy as np

def compute_scc(file, number_of_nodes):
    x, y = np.loadtxt(file, 'int', unpack = True)
    # adj_matrix = sparse.coo_matrix((np.ones(len(i_indices)), (i_indices, j_indices)), shape = (875715, 875715))
    # return connected_components(adj_matrix, connection = 'strong')

compute_scc('graf', 2)

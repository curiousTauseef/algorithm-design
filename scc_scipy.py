from scipy import sparse
import numpy as np

number_of_nodes = 875714

i_indices, j_indices = [], []
f = open('graf')
for line in f:
    i_index, j_index = line.split()
    i_indices.append(int(i_index))
    j_indices.append(int(j_index))
f.close()

adj_matrix = sparse.coo_matrix((np.ones(len(i_indices)), (i_indices, j_indices)), shape = (875715, 875715))
connected_components = sparse.csgraph.connected_components(adj_matrix, connection = 'strong')
components = sorted(np.bincount(connected_components[1]), reverse = True)
for i in range(5):
    print(components[i])

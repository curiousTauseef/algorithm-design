import sys
sys.path.append('../graph/')
from bellmanford import bellmanford, getpath
import graph_mat as graph

dist, pred = bellmanford(graph.read('../data/graph'), 109)
print ('Distance: {}'.format(dist[609]))
print ('Path: {}'.format(getpath(pred, 609)))

from floydwarshall import floydwarshall
import timeit
import sys
sys.path.append('../graph')

def test():
    floydwarshall(graph.read('../data/graph'))
 
import graph_list as graph
time_list = timeit.timeit('test()', setup='from __main__ import test', number = 1)
import graph_mat as graph
time_mat = timeit.timeit('test()', setup='from __main__ import test', number = 1)

print('List implementation: ')
print('Time: {}\n'.format(time_list))
print('Matrix implementation: ')
print('Time: {}\n'.format(time_mat))
print('R: {}'.format(time_list/time_mat))

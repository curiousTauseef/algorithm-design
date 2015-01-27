import numpy as np
class Graph:
  
  def __init__(self, n):
    self.arr = np.zeros((n, n))
    self.n = n

  def add_vertex(self):
    self.n += 1
    self.arr.resize(self.n, self.n)

  def del_vertex(vid):
    self.n -= 1
    self.arr[vid, :] = 0
    self.arr[:, vid] = 0
    
  def add_edge(self, vid1, vid2, cost):
    self.arr[vid1, vid2] = cost

  def del_edge(self, vid1, vid2):
    self.arr[vid1, vid2] = 0

  def get_children(self, vid):
    return np.nonzero(self.arr[vid, :])[0]

  def get_parents(self, vid):
    return np.nonzero(self.arr[:, vid])

  def get_out_edges(self, vid):
    return [(get_edge(vid, vertex)) for vertex in get_children(vid)]

  def get_in_edges(self, vid):
    return [(get_edge(vertex, vid)) for vertex in get_parents(vid)]

  def get_edge(self, vid1, vid2):
    return (vid1, vid2, self.arr[vid1, vid2])

  def get_dist(self, vid1, vid2):
    return (self.arr[vid1, vid2])

  def get_num_vertices(self):
    return self.n

  def get_num_edges(self):
    return np.count_nonzero(self.arr)

  def are_neighbors(self, vid1, vid2):
    return any([self.arr[vid1][vid2], self.arr[vid1][vid2]])

def read(file, n = 1000):
    graph = Graph(n)
    with open(file) as f:
        for line in f:
            line = [int (x) for x in line.strip().split()]
            graph.add_edge(line[0], line[1], line[2])
    return graph

import numpy as np

class Graph:
    def __init__(self, n):
        self.vertList = {}
        self.n = 0

    def addVertex(self, vid):
        if not self.is_vertex(vid):
            self.n += 1
            self.vertList[vid] = {}

    def del_vertex(vid):
        del self.vertList[vid]

    def add_edge(self, vid1, vid2, cost):
        self.addVertex(vid1)
        self.vertList[vid1][vid2] = cost

    def del_edge(self, vid1, vid2):
        del self.vertList[vid1][vid2]

    def get_children(self, vid):
        return list(self.vertList[vid].keys())

    def get_parents(self, vid):
        return [vertex for vertex in self.vertList.keys() if vid in vertList[vertex]]

    def get_out_edges(self, vid):
        return [(get_edge(vid, vertex)) for vertex in self.get_children(vid)]

    def get_in_edges(self, vid):
        return [(get_edge(vertex, vid)) for vertex in self.get_parents(vid)]

    def get_edge(self, vid1, vid2):
        return (vid1, vid2, self.get_dist(vid1, vid2))

    def get_dist(self, vid1, vid2):
        return self.vertList[vid1][vid2]

    def get_num_vertices(self):
        return self.n

    def is_vertex(self, vid):
        return vid in self.vertList.keys()

def read(file, n = 1000):
    graph = Graph(n)
    with open(file) as f:
        for line in f:
            line = [int (x) for x in line.strip().split()]
            graph.add_edge(line[0], line[1], line[2])
    return graph

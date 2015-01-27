def read(file, n = 1000):
    graph = Graph(n)
    with open(file) as f:
        for line in f:
            line = [int (x) for x in line.strip().split()]
            graph.add_edge(line[0], line[1], line[2])
    return graph

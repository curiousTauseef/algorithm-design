#ifndef GRAPH_H
#define GRAPH_H

#include <vector>

class Graph {
private:
    int adjacencyMatrixSize;
    int* adjacencyMatrix;
    int vertexCount;
public:
    Graph(int vertexCount);
    int getVertexCount();
    bool isValid(int vertex);
    void addEdge(int head, int tail, int cost);
    void removeEdge(int head, int tail);
    std::vector<int> getChildren(int parent);
    int getCost(int head, int tail);
};
#endif

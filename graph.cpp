#include <vector>
#include "graph.h"

Graph::Graph(int vertexCount)
    : vertexCount(vertexCount)
    , adjacencyMatrixSize(vertexCount*vertexCount)
    , adjacencyMatrix(new int[adjacencyMatrixSize]())
{}
int Graph::getVertexCount() {
    return vertexCount;
}
bool Graph::isValid(int vertex) {
    return (vertex >= 0 && vertex < vertexCount);
}
void Graph::addEdge(int head, int tail, int cost) {
    if (isValid(head) && isValid(tail))
	adjacencyMatrix[head + vertexCount*tail] = cost;
}
void Graph::removeEdge(int head, int tail) {
    if (isValid(head) && isValid(tail))
	adjacencyMatrix[head + vertexCount*tail] = 0;
}
std::vector<int> Graph::getChildren(int parent) {
    std::vector<int> children = std::vector<int>();
    if (isValid(parent)) {
	for (int child = 0; child < vertexCount; child++) {
	    if (adjacencyMatrix[parent + vertexCount*child] != 0)
		children.push_back(child);
	}
    }
    return children;
}
int Graph::getCost(int head, int tail) {
    return adjacencyMatrix[head + vertexCount*tail];
}

		


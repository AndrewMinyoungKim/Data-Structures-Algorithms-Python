def kruskal(graph):
    n = len(graph)

    visited = []

    while(len(visited) >= len(graph)):
        
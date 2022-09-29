from collections import deque

def bfs(node, graph):
    queue = deque()
    visited = []

    queue.append(node)
    visited.append(node)

    while(queue):
        s = queue.popleft()
        print(f"{s}")

        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
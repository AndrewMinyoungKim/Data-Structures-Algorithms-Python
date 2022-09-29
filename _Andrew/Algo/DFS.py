def dfs(node, graph):
    stack = []
    visited = []

    stack.append(node)
    visited.append(node)

    while stack:
        s = stack.pop()
        print(f"{s}")

        for i in reversed(graph[s]):
            if i not in visited:
                stack.append(i)
                visited.append(i)
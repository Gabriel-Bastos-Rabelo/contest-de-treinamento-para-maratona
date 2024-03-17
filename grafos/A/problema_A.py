def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    def bfs(residual_graph):
        visited = [False] * len(residual_graph)
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(residual_graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[sink]

    while bfs(graph):
        path_flow = float("Inf")
        s = sink

        while (s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while (v != source):
            u = parent[v]
            graph[u][v] -= path_flow
           
            v = parent[v]

    return max_flow


n, m = map(int, input().split())

graph = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


print(ford_fulkerson(graph, 1, n))

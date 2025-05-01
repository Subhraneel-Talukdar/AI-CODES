from collections import defaultdict
graph = defaultdict(list)
num_edges = int(input("Number of Edges: "))
for i in range(num_edges):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))
start_node = int(input("Starting Point: "))
dfs(start_node)

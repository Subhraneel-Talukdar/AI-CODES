from collections import deque, defaultdict
graph = defaultdict(list)
num_edges = int(input("Number of Edges: "))
for i in range(num_edges):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    graph[u].append(v)
    graph[v].append(u)
def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
start_node = int(input("Starting Point: "))
bfs(start_node)

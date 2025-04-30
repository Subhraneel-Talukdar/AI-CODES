from collections import deque, defaultdict

print("== Breadth-First Search Algorithm ==")

# Create an undirected graph
graph = defaultdict(list)
edge_count = int(input("\nEnter number of edges: "))
print("Enter each edge as 'source destination' (e.g., '1 2'):")
for i in range(edge_count):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# Print the graph structure
print("\nGraph structure:")
for node in sorted(graph):
    print(f"Node {node} connected to: {sorted(graph[node])}")


def bfs(start):
    print(f"\nBFS traversal starting from node {start}:")
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])


# Start BFS traversal
start_node = int(input("\nEnter starting node for BFS: "))
bfs(start_node)
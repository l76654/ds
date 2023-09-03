import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
    
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append((to_node, cost))
        self.edges[to_node].append((from_node, cost))  # Assuming an undirected graph

def astar(graph, start, goal):
    open_list = [(0, start)]  # Priority queue of (f_score, node)
    came_from = {}  # Dictionary to track the parent of each node
    g_score = {node: float('inf') for node in graph.nodes}  # Cost from start to node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}  # Estimated total cost from start to goal through node
    f_score[start] = heuristic(start, goal)  # Initial estimate

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph.edges[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

def heuristic(node, goal):
    # In this example, we use the Euclidean distance as the heuristic
    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Example usage:
graph = Graph()
graph.add_node((0, 0))
graph.add_node((1, 2))
graph.add_node((2, 2))
graph.add_node((2, 0))
graph.add_edge((0, 0), (1, 2), 2)
graph.add_edge((0, 0), (2, 2), 3)
graph.add_edge((1, 2), (2, 0), 4)
graph.add_edge((2, 2), (2, 0), 1)

start_node = (0, 0)
goal_node = (2, 0)

path = astar(graph, start_node, goal_node)

if path:
    print("Shortest Path:", path)
else:
    print("No path found.")

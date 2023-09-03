import itertools

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_path = None
    shortest_distance = float('inf')

    for path in itertools.permutations(cities):
        if path[0] == 0:  # Start from city 0
            total_distance = calculate_total_distance(path, distances)
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path

    return shortest_path, shortest_distance

# Example usage:
# Define the distance matrix between cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, shortest_distance = traveling_salesman_bruteforce(distances)

if shortest_path:
    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
else:
    print("No solution found.")

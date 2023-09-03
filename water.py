from collections import deque

def pour(jug, max_capacity):
    return 0 if jug == 0 else max_capacity

def water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited = set()
    queue = deque([(0, 0)])  # Initial state of jugs

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if jug1 == target or jug2 == target:
            return current_state

        visited.add(current_state)

  
        for new_state in [(capacity_jug1, jug2), (jug1, capacity_jug2)]:
            if new_state not in visited:
                queue.append(new_state)

        # Empty jug1 and jug2
        for new_state in [(0, jug2), (jug1, 0)]:
            if new_state not in visited:
                queue.append(new_state)

       
        for new_state in [
            (min(jug1 + jug2, capacity_jug1), max(0, jug1 + jug2 - capacity_jug1)),
            (max(0, jug1 + jug2 - capacity_jug2), min(jug1 + jug2, capacity_jug2))
        ]:
            if new_state not in visited:
                queue.append(new_state)

    return None

jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
target_amount = int(input("Enter the target amount of water: "))

solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

if solution:
    print(f"Solution found: Fill the first jug with {solution[0]} units and the second jug with {solution[1]} units.")
else:
    print("No solution found.")

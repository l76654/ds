from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 1)  # (Missionaries on the left, Cannibals on the left, Boat position)
goal_state = (0, 0, 0)

def is_valid_state(state):
    # Check if the number of Cannibals on either side is greater than or equal to Missionaries
    if state[0] < state[1] and state[0] > 0:
        return False
    if 3 - state[0] < 3 - state[1] and 3 - state[0] > 0:
        return False
    return True

def get_next_states(current_state):
    next_states = []
    boat = current_state[2]
    
    # Generate possible actions (moving 1 or 2 people)
    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for action in actions:
        if boat == 1:
            next_state = (
                current_state[0] - action[0],
                current_state[1] - action[1],
                0  # Move the boat to the right
            )
        else:
            next_state = (
                current_state[0] + action[0],
                current_state[1] + action[1],
                1  # Move the boat to the left
            )
        
        if is_valid_state(next_state) and (next_state[0] >= 0 and next_state[0] <= 3) and (next_state[1] >= 0 and next_state[1] <= 3):
            next_states.append(next_state)
    
    return next_states

def bfs():
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)
        
        if current_state == goal_state:
            return path
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

path_to_goal = bfs()

if path_to_goal:
    print("Solution found:")
    for i, state in enumerate(path_to_goal):
        print(f"Step {i + 1}: {state}")
else:
    print("No solution found.")

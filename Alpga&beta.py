game_tree = {
    'A': {'value': 0, 'children': ['B', 'C', 'D']},
    'B': {'value': 3, 'children': ['E', 'F', 'G']},
    'C': {'value': 5, 'children': ['H', 'I', 'J']},
    'D': {'value': 6, 'children': ['K', 'L', 'M']},
    'E': {'value': 2, 'children': []},
    'F': {'value': 9, 'children': []},
    'G': {'value': 8, 'children': []},
    'H': {'value': 1, 'children': []},
    'I': {'value': 7, 'children': []},
    'J': {'value': 4, 'children': []},
    'K': {'value': 0, 'children': []},
    'L': {'value': 2, 'children': []},
    'M': {'value': 3, 'children': []},
}

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not game_tree[node]['children']:
        return game_tree[node]['value']

    if maximizing_player:
        max_eval = float('-inf')
        for child_node in game_tree[node]['children']:
            eval = alpha_beta_pruning(child_node, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child_node in game_tree[node]['children']:
            eval = alpha_beta_pruning(child_node, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def main():
    best_score = alpha_beta_pruning('A', 3, float('-inf'), float('inf'), True)
    print("Best Score:", best_score)

if __name__ == "__main__":
    main()

class MapColoringCSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables  # List of variable names (regions)
        self.domains = domains  # Dictionary of variable domains (colors)
        self.neighbors = neighbors  # Dictionary of neighboring regions
        self.constraints = constraints  # List of constraint functions

    def is_consistent(self, assignment, var, value):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  # All variables are assigned

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(assignment, var, value):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None  # No solution found

    def select_unassigned_variable(self, assignment):
        unassigned = [var for var in self.variables if var not in assignment]
        return unassigned[0]

    def order_domain_values(self, var, assignment):
        return self.domains[var]

def main():
    # Define the regions and their colors
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    colors = {'R', 'G', 'B'}

    # Define the neighbors of each region
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    # Define the constraint function
    def not_equal(var1, var2, value1, value2):
        return value1 != value2

    constraints = [not_equal]

    # Create the Map Coloring CSP instance
    map_coloring = MapColoringCSP(regions, {region: colors for region in regions}, neighbors, constraints)

    # Solve the problem
    solution = map_coloring.backtracking_search()

    if solution:
        print("Map Coloring Solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

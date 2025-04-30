import random

# Parameters
POP_SIZE = 50
GENERATIONS = 200
MUTATION_RATE = 0.02

# Get distance matrix from user
def get_distance_matrix():
    n = int(input("Enter number of cities: "))
    print(f"Enter {n} rows of {n} distances (e.g., '0 10 15 ...')")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"City {i+1}: ").split()))
        matrix.append(row)
    return matrix


# Calculate route distance
def route_distance(route, dist_matrix):
    total = 0
    # Sum distances between consecutive cities in the route
    for i in range(len(route) - 1):
        total += dist_matrix[route[i]][route[i + 1]]
    # Add distance from the last city back to the starting city
    total += dist_matrix[route[-1]][route[0]]  # Return to start
    return total


# Create random route, ensuring it starts with start
def create_route(n, start):
    # Create a list of city indices [0, 1, ..., n-1]
    cities = list(range(n))
    # Remove the designated start city
    cities.remove(start)
    # Shuffle the remaining cities randomly
    random.shuffle(cities)
    # Create the route starting with start, followed by the shuffled rest
    route = [start] + cities
    return route


# Crossover (ordered crossover)
def crossover(p1, p2):
    # Select two random indices for the crossover segment
    start, end = sorted(random.sample(range(len(p1)), 2))
    # Initialize child route with placeholders (-1)
    child = [-1] * len(p1)
    # Copy the segment from the first parent (p1) to the child
    child[start:end] = p1[start:end]
    # Get cities from the second parent (p2) that are not already in the child's segment
    remaining = [x for x in p2 if x not in child[start:end]]
    # Fill the remaining placeholder slots in the child with cities from 'remaining'
    for i in range(len(p1)):
        if child[i] == -1:
            child[i] = remaining.pop(0)
    return child


# Mutation (swap two cities, excluding the start city)
# Use global MUTATION_RATE
def mutate(route):
    # Perform mutation only if a random number is less than the mutation rate
    if random.random() < MUTATION_RATE:
        # Select two distinct random indices *from the non-starting cities*
        # Ensure we have at least 2 cities other than the start city to swap
        if len(route) > 2:
            i, j = random.sample(range(1, len(route)), 2) # Sample from index 1 onwards
            # Swap the cities at these indices
            route[i], route[j] = route[j], route[i]
    return route


# Genetic Algorithm
# Use global constants, accept start
def solve_tsp(dist_matrix, start):
    n = len(dist_matrix) # Number of cities
    # Initialize population with POP_SIZE random routes, all starting at start
    population = [create_route(n, start) for _ in range(POP_SIZE)]

    # Run the genetic algorithm for a fixed number of generations
    for gen in range(GENERATIONS):
        # Sort the population by route distance (ascending - shorter is better)
        population.sort(key=lambda x: route_distance(x, dist_matrix)) # Sort by distance (fitness)
        # Start building the next generation, keeping the best route from the current one (elitism)
        new_pop = [population[0]]  # Keep best

        # Fill the rest of the new population until it reaches POP_SIZE
        while len(new_pop) < POP_SIZE:
            # Select two parent routes from the top 10 fittest individuals
            p1, p2 = random.choices(population[:10], k=2)  # Pick from top 10
            # Create a child route by combining the parents
            child = crossover(p1, p2)
            # Add the (potentially mutated) child to the new population
            # Call mutate without arguments
            new_pop.append(mutate(child))

        # Replace the old population with the newly generated one
        population = new_pop
        # Print progress every 50 generations (or adjust frequency if needed)
        # Also print the last generation's result
        if gen % 50 == 0 or gen == GENERATIONS - 1:
            print(f"Gen {gen}: Distance = {route_distance(population[0], dist_matrix)}")

    # After all generations, the best route is the first one in the sorted population
    best_route = population[0]
    # Return the best route found and its total distance
    return best_route, route_distance(best_route, dist_matrix)


# Get the starting city from the user
def get_start_city(n): # Renamed parameter
    while True:
        try:
            # Updated f-string to use n
            start_input = int(input(f"Enter the starting city index (0 to {n - 1}): "))
            if 0 <= start_input < n: # Use n for comparison
                return start_input # Return the valid starting city index
            else:
                print("Invalid index. Please enter a value within the range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Run it
# Get the distance matrix from the user
dist_matrix = get_distance_matrix()
n = len(dist_matrix) # Renamed variable

# Get the starting city using the new function
start = get_start_city(n) # Pass n to the function

# Print the entered matrix for verification
print("\nDistance Matrix:")
for row in dist_matrix:
    print(row)
# Solve the TSP using the genetic algorithm, providing the start city
# Call solve_tsp with start argument
best_route, best_dist = solve_tsp(dist_matrix, start)

# Print the best route found
print(f"\nBest Route: {best_route}")
# Print the distance of the best route
print(f"Best Distance: {best_dist}")

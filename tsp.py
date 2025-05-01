import random

POP_SIZE = 50
GENERATIONS = 200
MUTATION_RATE = 0.02

def get_distance_matrix():
    n = int(input("Enter number of cities: "))
    print(f"Enter {n} rows of {n} distances (e.g., '0 10 15 ...')")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"City {i+1}: ").split()))
        matrix.append(row)
    return matrix


def route_distance(route, dist_matrix):
    total = 0

    for i in range(len(route) - 1):
        total += dist_matrix[route[i]][route[i + 1]]
    
    total += dist_matrix[route[-1]][route[0]]  # Return to start
    return total


def create_route(n, start):
    cities = list(range(n))
    cities.remove(start)
    random.shuffle(cities)
    route = [start] + cities
    return route


def crossover(p1, p2):
    start, end = sorted(random.sample(range(len(p1)), 2))
    child = [-1] * len(p1)
    child[start:end] = p1[start:end]
    remaining = [x for x in p2 if x not in child[start:end]]
    for i in range(len(p1)):
        if child[i] == -1:
            child[i] = remaining.pop(0)
    return child


def mutate(route):
    if random.random() < MUTATION_RATE:
        if len(route) > 2:
            i, j = random.sample(range(1, len(route)), 2)
            route[i], route[j] = route[j], route[i]
    return route


def solve_tsp(dist_matrix, start):
    n = len(dist_matrix)
    population = [create_route(n, start) for _ in range(POP_SIZE)]

    for gen in range(GENERATIONS):
       
        population.sort(key=lambda x: route_distance(x, dist_matrix)) 
        new_pop = [population[0]]  # Keep best

        while len(new_pop) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)
            child = crossover(p1, p2)
            new_pop.append(mutate(child))

        population = new_pop
        if gen % 50 == 0 or gen == GENERATIONS - 1:
            print(f"Gen {gen}: Distance = {route_distance(population[0], dist_matrix)}")

    best_route = population[0]
    return best_route, route_distance(best_route, dist_matrix)


def get_start_city(n):
    while True:
        try:
            start = int(input(f"Enter the starting city index (0 to {n - 1}): "))
            if 0 <= start < n: 
                return start 
            else:
                print("Invalid index. Please enter a value within the range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


dist_matrix = get_distance_matrix()
n = len(dist_matrix)

start = get_start_city(n)

print("\nDistance Matrix:")
for row in dist_matrix:
    print(row)
    
best_route, best_dist = solve_tsp(dist_matrix, start)

print(f"\nBest Route: {best_route}")
print(f"Best Distance: {best_dist}")
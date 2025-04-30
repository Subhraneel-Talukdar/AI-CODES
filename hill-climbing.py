import numpy as np
import matplotlib.pyplot as plt


def generate_neighbours(x, step_size=1):
    """Generate neighboring points by moving step_size in both directions.
    
    Args:
        x: Current point
        step_size: Distance to move in each direction
        
    Returns:
        List of neighboring points
    """
    return [x - step_size, x + step_size]


def hill_climbing(f, x0, max_iterations=1000, step_size=1):
    """Perform hill climbing optimization to find local maximum.
    
    Args:
        f: Objective function to maximize
        x0: Initial starting point
        max_iterations: Maximum number of iterations
        step_size: Step size for generating neighbors
        
    Returns:
        Tuple of (best_x, path)
    """
    x = x0
    iterations = 0
    path = [x]
    
    print("\nStarting hill climbing from x =", x)
    print("-" * 40)
    
    while iterations < max_iterations:
        neighbours = generate_neighbours(x, step_size)
        best_neighbour = max(neighbours, key=f)
        
        current_value = f(x)
        best_value = f(best_neighbour)
        
        print(f"Iteration {iterations+1}: Current x = {x}, f(x) = {current_value:.4f}")
        print(f"  Best neighbor: x = {best_neighbour}, f(x) = {best_value:.4f}")
        
        # Check if we've reached a local maximum
        if best_value <= current_value:
            print(f"\nLocal maximum found at x = {x} with value f(x) = {current_value:.4f}")
            return x, path
            
        x = best_neighbour
        path.append(x)
        iterations += 1
        
        if iterations % 5 == 0:
            print("-" * 40)
    
    print(f"\nReached maximum iterations. Best point: x = {x} with value f(x) = {f(x):.4f}")
    return x, path


if __name__ == "__main__":
    print("=" * 60)
    print("HILL CLIMBING ALGORITHM VISUALIZATION")
    print("=" * 60)
    
    # Get user input with better prompts and error handling
    try:
        expr = input("\nEnter the function to maximize (in terms of x)\n" +
                    "Example: x**2 - 4*x + 4\n> ")
        
        # Test the function to ensure it's valid
        test_value = 1
        f = lambda x: eval(expr, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, 
                                 "exp": np.exp, "sqrt": np.sqrt, "pi": np.pi})
        f(test_value)  # This will raise an exception if there's a problem
        
        # Get initial value and step size
        x0 = float(input("\nEnter initial x value: "))
        step_size = float(input("Enter step size (default=1): ") or "1")
        
        # Run hill climbing
        result, path = hill_climbing(f, x0, step_size=step_size)
        
        # Visualization with improved formatting
        plt.figure(figsize=(10, 6))
        
        # Compute appropriate range for x values
        path_min, path_max = min(path), max(path)
        range_extension = max(10, (path_max - path_min) * 0.5)  # At least 10, or 50% of the path range
        x_min, x_max = path_min - range_extension, path_max + range_extension
        
        x_values = np.linspace(x_min, x_max, 500)
        y_values = [f(x) for x in x_values]
        
        # Plot the function and path
        plt.plot(x_values, y_values, label=f"Function: {expr}", linewidth=2)
        plt.scatter(path, [f(x) for x in path], color="red", marker="o", s=50, 
                   label="Hill Climbing Path")
        
        # Mark start and end points
        plt.scatter([path[0]], [f(path[0])], color="green", marker="^", s=100, 
                   label="Start Point")
        plt.scatter([path[-1]], [f(path[-1])], color="blue", marker="*", s=150, 
                   label="End Point (Local Maximum)")
        
        # Improve plot styling
        plt.xlabel("x", fontsize=12)
        plt.ylabel("f(x)", fontsize=12)
        plt.title(f"Hill Climbing Algorithm Visualization\nFunction: {expr}", fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        
        print("\nDisplaying visualization. Close the plot window to exit.")
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"\nError: {e}")
        print("Please try again with a valid function expression.")
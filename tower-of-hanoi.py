def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 0:
        return 0
    moves = 0
    # Move n-1 disks from source to auxiliary, using destination as auxiliary
    moves += tower_of_hanoi(n - 1, source, auxiliary, destination)
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    moves += 1
    # Move the n-1 disks from auxiliary to destination, using source as auxiliary
    moves += tower_of_hanoi(n - 1, auxiliary, destination, source)
    return moves


while True:
    try:
        num_disks = int(input("Enter the number of disks (non-negative integer): "))
        if num_disks >= 0:
            break
        else:
            print("Number of disks cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f"\nSolving Tower of Hanoi for {num_disks} disks using towers A, B, C:")

if num_disks > 0:
    total_moves = tower_of_hanoi(num_disks, 'A', 'C', 'B')
    print(f"\nTotal number of moves: {total_moves}")
else:
    print("\nTotal number of moves: 0")

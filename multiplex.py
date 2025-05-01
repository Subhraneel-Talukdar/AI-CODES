from collections import deque, defaultdict
distances = set(map(int, input("Enter distances of multiplexes from residence (space-separated): ").split()))
action_multiplexes = set(map(int, input("Enter distances of multiplexes playing action movies (space-separated): ").split()))
parking_availability = defaultdict(bool)
print("Enter parking availability for action movie multiplexes:")
for multiplex in action_multiplexes:
    parking_status = (input(f"Parking available at multiplex {multiplex} km? (y/n): ").strip().lower())
    parking_availability[multiplex] = parking_status == "y"
def bfs():
    queue = deque(sorted(list(distances)))
    while queue:
        multiplex = queue.popleft()
        if multiplex in action_multiplexes and parking_availability[multiplex]:
            print(f"\nSelected Multiplex: The one at {multiplex} km distance.")
            return
    print("\nNo suitable multiplex found (Action movie playing + Parking available).")
bfs()

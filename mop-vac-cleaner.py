row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix = [[0] * col for _ in range(row)]
print("Simulating Cleaner Movement:")
for i in range(row):
    if i % 2 == 0:
        for j in range(col):
            matrix[i][j] = 1
            print(f"Cleaned ({i},{j}):")
            for r in matrix: print(r)
            print("---")
    else:
        for j in range(col - 1, -1, -1):
            matrix[i][j] = 1
            print(f"Cleaned ({i},{j}):")
            for r in matrix: print(r)
            print("---")
print("\nFinal Cleaning Area: ")
for r in matrix: print(r)

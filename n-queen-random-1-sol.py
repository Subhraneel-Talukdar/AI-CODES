import random
def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve_n_queens(N):
    board = [-1] * N
    def backtrack(row):
        if row == N:
            return True
        for col in random.sample(range(N), N):
            if is_safe(board, row, col, N):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False
    backtrack(0)
    return board
def print_board(board):
    N = len(board)
    if -1 in board:
        print(f"No solution found for N={N} with this random try.")
        return
    print(f"Solution for N={N}:")
    for r in range(N):
        row_str = ""
        for c in range(N):
            if board[r] == c:
                row_str += "Q "
            else:
                row_str += ". "
        print(row_str.strip())
N = int(input("Enter the number of queens (N): "))
if N < 4 and N != 1:
    print(f"No solution exists for N={N}.")
elif N == 1:
    print("Solution for N=1:")
    print("Q")
else:
    solution_board = solve_n_queens(N)
    print_board(solution_board)

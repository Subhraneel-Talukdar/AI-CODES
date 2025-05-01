import math
def show(b):
    for r in b:
        print(" | ".join(c if c != " " else "_" for c in r))
        print("-" * 9)
def win(b):
    lines = (
        b
        + [list(c) for c in zip(*b)]
        + [[b[i][i] for i in range(3)], [b[i][2 - i] for i in range(3)]]
    )
    for l in lines:
        if len(set(l)) == 1 and l[0] != " ":
            return l[0]
    if all(c != " " for r in b for c in r):
        return "Draw"
    return None
def mini(b, ai):
    r = win(b)
    if r:
        return {"X": -1, "O": 1, "Draw": 0}[r]
    scores = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                b[i][j] = "O" if ai else "X"
                scores.append(mini(b, not ai))
                b[i][j] = " "
    return max(scores) if ai else min(scores)
def best(b):
    m, s = None, -math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                b[i][j] = "O"
                sc = mini(b, False)
                b[i][j] = " "
                if sc > s:
                    s = sc
                    m = (i, j)
    return m
def play():
    b = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe: You are X, AI is O")
    show(b)
    while True:
        while True:
            try:
                r, c = map(int, input("Your move (row col, 0-2): ").split())
                if 0 <= r <= 2 and 0 <= c <= 2 and b[r][c] == " ":
                    b[r][c] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and col (0-2).")
        show(b)
        r = win(b)
        if r:
            print(f"{r} wins!" if r != "Draw" else "It's a Draw!")
            break
        print("AI ('O') is thinking...")
        r, c = best(b)
        b[r][c] = "O"
        show(b)
        r = win(b)
        if r:
            print(f"{r} wins!" if r != "Draw" else "It's a Draw!")
            break
play()

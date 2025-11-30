pos = input("Введіть позицію слона (наприклад, g4): ").strip()
col = ord(pos[0]) - ord('a')
row = int(pos[1]) - 1
board = [["." for _ in range(8)] for _ in range(8)]
board[row][col] = "B"
directions = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
for dr, dc in directions:
    r, c = row + dr, col + dc
    while 0 <= r < 8 and 0 <= c < 8:
        board[r][c] = "*"
        r += dr
        c += dc
for r in range(7, -1, -1):
    print(" ".join(board[r]))
# 🎁 Part 1: Find the Magic Word 
def count_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Directions: Right, Down, Diagonals, etc.
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),
        (0, -1), (-1, 0), (-1, -1), (-1, 1)
    ]

    def is_word_at(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if is_word_at(r, c, dr, dc):
                    count += 1

    return count


# ✨ Part 2: The X-MAS Hunt 
def count_xmas_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Possible "MAS" combinations
    mas_patterns = [("M", "A", "S"), ("S", "A", "M"), ("S", "S", "M"), ("M", "M", "S")]

    def is_xmas_at(r, c):
        if grid[r][c] != "A":  # The center must be the shining "A"
            return False

        diagonals = [
            ((r - 1, c - 1), (r + 1, c + 1)),  # Top-left to bottom-right
            ((r - 1, c + 1), (r + 1, c - 1))   # Top-right to bottom-left
        ]

        def is_mas(diagonal):
            (r1, c1), (r2, c2) = diagonal
            if 0 <= r1 < rows and 0 <= c1 < cols and 0 <= r2 < rows and 0 <= c2 < cols:
                char1, char2 = grid[r1][c1], grid[r2][c2]
                return any((char1, "A", char2) == pattern for pattern in mas_patterns)
            return False

        # Check if both diagonals create the festive "X-MAS"
        return is_mas(diagonals[0]) and is_mas(diagonals[1])

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_xmas_at(r, c):
                count += 1

    return count


# Load the Christmas grid
with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Find "XMAS" magic words
word_to_find = "XMAS"
result = count_word_in_grid(grid, word_to_find)
print(f"🎁 The word '{word_to_find}' appears {result} times! 🎄")

# Find "X-MAS" patterns
result2 = count_xmas_patterns(grid)
print(f"🎅 The X-MAS pattern appears {result2} times! 🎁")


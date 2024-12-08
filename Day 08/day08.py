import math

def parse_input(grid):
    positions = {}
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != '.':  # Ignore empty spaces
                if char not in positions:
                    positions[char] = []
                positions[char].append((i, j))
    return positions

# Part 1
def create_antinode(positions, grid):
    rows = len(grid)
    cols = len(grid[0])
    antinode = set()

    for char, pos in positions.items():
        for p in pos:
            for q in pos:
                if p != q:
                    xm = 2 * q[0] - p[0]
                    ym = 2 * q[1] - p[1]
                    if 0 <= xm < rows and 0 <= ym < cols:
                        antinode.add((xm, ym))
    return antinode

# Part 2
def create_antinode_update(positions, grid):
    rows = len(grid)
    cols = len(grid[0])
    antinode = set()

    for char, pos in positions.items():
        for p in pos:
            for q in pos:
                if p != q:
                    # Calculate direction vector and magnitude
                    dir_x, dir_y = q[0] - p[0], q[1] - p[1]
                    magnitude = math.sqrt(dir_x ** 2 + dir_y ** 2)
                    
                    if magnitude == 0:  # Avoid division by zero
                        continue
                    
                    magnitude_floor = math.floor(magnitude)
                    k_max = math.floor(min(rows, cols) / magnitude_floor)
                    
                    # Generate all positions in the antinode
                    for k in range(-k_max, k_max + 1):
                        xm = q[0] + k * dir_x
                        ym = q[1] + k * dir_y
                        if 0 <= xm < rows and 0 <= ym < cols:
                            antinode.add((xm, ym))
    
    return antinode

input_path = "input.txt"
with open(input_path, "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Part 1: Calculate antinodes
antennas = parse_input(grid)
antinodes = create_antinode(antennas, grid)

print(f"Part 1: Total unique antinodes: {len(antinodes)} 🎁🎅")

# Part 2: Calculate enhanced antinodes
antinodes2 = create_antinode_update(antennas, grid)

print(f"Part 2: Total unique antinodes after harmonic update: {len(antinodes2)} 🎄✨")


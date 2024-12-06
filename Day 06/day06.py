def parse_input(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f]
    return grid


# 🎄🎅 Part 1: Simulate the guard's path 🎅🎄
def simulate_guard(grid):
    
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Find the starting position and direction
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in directions:
                pos = (r, c)
                direction = char
                break

    visited = set()
    rows, cols = len(grid), len(grid[0])
    
    while True:
        visited.add(pos)  # Add position to the list of visited places
        r, c = pos
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc
        
        # Check if we are out of bounds 
        if not (0 <= nr < rows and 0 <= nc < cols):
            break
        
        # Check for obstacles 
        if grid[nr][nc] == '#':
            direction = turns[direction]  # ↩ Turn right 
        else:
            pos = (nr, nc)  # 🚶 Move forward 

    return len(visited)


# 🎄🎅 Part 2: Simulate with obstructions to trap the guard 🎅🎄
def simulate_with_obstruction(grid, obstruction):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    # 🔍 Find the starting position and direction 
    start_pos, direction = None, None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in directions:
                start_pos = (r, c)
                direction = char
                break

    if not start_pos:
        raise ValueError("🎅🎄 Starting position not found! 🎄🎅")

    visited_states = set()
    pos = start_pos
    rows, cols = len(grid), len(grid[0])

    # Add the obstruction 
    original = grid[obstruction[0]][obstruction[1]]
    grid[obstruction[0]][obstruction[1]] = '#'

    while True:
        # Check current state (position + direction) 
        state = (pos, direction)
        if state in visited_states:
            grid[obstruction[0]][obstruction[1]] = original  # Restore 
            return True  # Guard is trapped in a loop! 
        visited_states.add(state)

        r, c = pos
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        # Check if we are out of bounds 
        if not (0 <= nr < rows and 0 <= nc < cols):
            break

        # Check for obstacles 
        if grid[nr][nc] == '#':
            direction = turns[direction]  # ↩ Turn right 
        else:
            pos = (nr, nc)  # 🚶 Move forward 

    grid[obstruction[0]][obstruction[1]] = original  # Restore 
    return False  # No loop found 

def find_possible_obstructions(grid):
    rows, cols = len(grid), len(grid[0])
    possible_positions = []

    for r in range(rows):
        for c in range(cols):
            # Exclude starting position and existing obstacles 
            if grid[r][c] == '.' and all(grid[r][c] != char for char in '^v<>'):
                if simulate_with_obstruction(grid, (r, c)):
                    possible_positions.append((r, c))

    return len(possible_positions), possible_positions



input_file = 'input.txt'
grid = parse_input(input_file)

# Part 1: Simulate the guard's path 
distinct_positions = simulate_guard(grid)
print(f"🎄 Number of distinct positions visited: {distinct_positions} 🎄")

# Part 2: Find obstructions to trap the guard (This might take a while ⏳)
count, positions = find_possible_obstructions(grid)
print(f"🎅 Number of possible positions for obstructions: {count} 🎅")
print(f"Positions causing loops: {positions} ")
print("oh oh oh, We have finished!!! 🎅🎅🎅 ")


def solve():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    grid = [list(map(int, list(line))) for line in lines]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Four directions: up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # PART 1
    memo_reachable_9 = {}

    def dfs_reachable_9(r, c):
        if (r, c) in memo_reachable_9:
            return memo_reachable_9[(r, c)]

        current_height = grid[r][c]
        # If we're at a '9', the set of reachable 9s is just this tile.
        if current_height == 9:
            memo_reachable_9[(r, c)] = {(r, c)}
            return memo_reachable_9[(r, c)]

        result = set()
        # Explore neighbors of height current_height + 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if valid(nr, nc) and grid[nr][nc] == current_height + 1:
                result = result.union(dfs_reachable_9(nr, nc))

        memo_reachable_9[(r, c)] = result
        return result

    # PART 2
    memo_path_count = {}

    def dfs_count_paths(r, c):
        if (r, c) in memo_path_count:
            return memo_path_count[(r, c)]

        current_height = grid[r][c]
        # If height is 9, there's exactly one path that ends here
        if current_height == 9:
            memo_path_count[(r, c)] = 1
            return 1

        total_paths = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if valid(nr, nc) and grid[nr][nc] == current_height + 1:
                total_paths += dfs_count_paths(nr, nc)

        memo_path_count[(r, c)] = total_paths
        return total_paths

    # Identify trailheads (cells of height 0) and accumulate score & rating
    total_score = 0
    total_rating = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Score: number of distinct '9' tiles reachable
                reachable_nines = dfs_reachable_9(r, c)
                trail_score = len(reachable_nines)
                total_score += trail_score

                # Rating: number of distinct paths to '9'
                trail_rating = dfs_count_paths(r, c)
                total_rating += trail_rating


    print("🎅 Ho-ho-ho! The total score of all trailheads is:", total_score, "🎄")
    print("🦌 The total rating (count of distinct hiking trails) of all trailheads is:", total_rating, "❄️")

if __name__ == "__main__":
   solve()


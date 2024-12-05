from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().strip()
    
    rules_section, updates_section = data.split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_section.splitlines()]
    return rules, updates


def validate_update(rules, update):
    position = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position:  
            if position[x] >= position[y]:  
                return False
    return True


def reorder_update(rules, update):
    # Build a directed graph for the pages in this update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)
    
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x]  # Ensure all nodes appear in in_degree

    
    queue = deque([page for page in update if in_degree[page] == 0])
    ordered_update = []

    while queue:
        current = queue.popleft()
        ordered_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update


def find_middle(page_list):
    return page_list[len(page_list) // 2]


def solve_puzzle(file_path):
    rules, updates = parse_input(file_path)
    
    valid_updates = []
    invalid_updates = []

    
    for update in updates:
        if validate_update(rules, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
   
    part1_result = sum(find_middle(update) for update in valid_updates)

    
    reordered_updates = [reorder_update(rules, update) for update in invalid_updates]
    
    
    part2_result = sum(find_middle(update) for update in reordered_updates)
    
    return part1_result, part2_result


# Run the solution
file_path = "input.txt"
part1_result, part2_result = solve_puzzle(file_path)

print(f"🎄 Part 1: The sum of middle page numbers for valid updates is: {part1_result} 🎅")
print(f"🎄 Part 2: The sum of middle page numbers for reordered updates is: {part2_result} 🎁")

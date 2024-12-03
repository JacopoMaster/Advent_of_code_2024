import re

def extract_and_sum_multiplications(file_path):
    """
    🎄 Part 1: Extracts all valid `mul(X,Y)` instructions and sums their results. 🎁
    """
    total_sum = 0
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    
    with open(file_path, 'r') as file:
        data = file.read()
        
        matches = re.findall(mul_pattern, data)
        for match in matches:
            numbers = re.findall(r"\d+", match)
            x, y = map(int, numbers)
            product = x * y
            total_sum += product
            print(f"Part 1: Found instruction {match} -> {x} * {y} = {product}")
    
    return total_sum

def process_memory(file_path):
    """
    🎄 Part 2: Process a corrupted memory file to calculate the total of enabled `mul(X, Y)` instructions
    while respecting `do()` and `don't()` instructions. 🎁
    """

    with open(file_path, "r") as file:
        corrupted_memory = file.read()
    
    # Regex patterns 
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Collect all occurrences of `mul`, `do`, and `don't` with their positions
    events = []
    for match in re.finditer(do_pattern, corrupted_memory):
        events.append((match.start(), "do"))
    for match in re.finditer(dont_pattern, corrupted_memory):
        events.append((match.start(), "don't"))
    for match in re.finditer(mul_pattern, corrupted_memory):
        x, y = match.groups()
        events.append((match.start(), "mul", int(x), int(y)))
    
    # Sort events by position in the string
    events.sort(key=lambda x: x[0])
    
    # Process events
    enabled = True  
    total = 0
    for event in events:
        if event[1] == "do":
            enabled = True
        elif event[1] == "don't":
            enabled = False
        elif event[1] == "mul" and enabled:
            total += event[2] * event[3]
    
    return total



file_path = 'input.txt'  

part1_result = extract_and_sum_multiplications(file_path)
print(f"🎄 Total sum of all valid multiplications: {part1_result} 🎉")


result = process_memory(file_path)
print(f"🎄 Total sum of enabled multiplications: {result} 🎉")

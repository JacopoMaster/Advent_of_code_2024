input_file = "input.txt"
with open(input_file, "r") as file:
    lines = file.readlines()

# 🎄 Part 1
def can_produce_target(numbers, target):
    from itertools import product
    
    # Generate all combinations of operators (+, *)
    operator_combinations = product(["+", "*"], repeat=len(numbers) - 1)
    for ops in operator_combinations:
        # Evaluate the expression left-to-right
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i + 1]
            elif op == "*":
                result *= numbers[i + 1]
        # Check if the result matches the target 
        if result == target:
            return True
    return False

# Parse the input and check each equation 
total_calibration_result = 0
for line in lines:
    if not line.strip():
        continue  # Skip empty lines 
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # Check if the equation can be true
    if can_produce_target(numbers, target):
        total_calibration_result += target



# 🎄 Part 2
def can_produce_target_extended(numbers, target):
    from itertools import product
    
    # Generate all combinations of operators (+, *, ||)
    operator_combinations = product(["+", "*", "||"], repeat=len(numbers) - 1)
    for ops in operator_combinations:
        # Evaluate the expression left-to-right
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i + 1]
            elif op == "*":
                result *= numbers[i + 1]
            elif op == "||":
                # Concatenate as a number, not a string 
                result = int(str(result) + str(numbers[i + 1]))
        # Check if the result matches the target 
        if result == target:
            return True
    return False

# Recalculate the total 
total_calibration_result_extended = 0
for line in lines:
    if not line.strip():
        continue  # Skip empty lines 
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # Check 
    if can_produce_target_extended(numbers, target):
        total_calibration_result_extended += target

# 🎉🎄 Final Results 🎄🎉
print(f"Total Calibration Result (Part 1): {total_calibration_result} 🎄✨")
print(f"Extended Total Calibration Result (Part 2): {total_calibration_result_extended} 🎄✨")




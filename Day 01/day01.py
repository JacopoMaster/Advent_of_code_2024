import numpy as np
from collections import Counter

# 🎄 Load the data 🎄
file_path = "input.txt"

left_list = []
right_list = []


with open(file_path, 'r') as file:
    for line in file:
        if line.strip():  # Salta le righe vuote
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)


left_sorted = np.sort(left_list)
right_sorted = np.sort(right_list)

# first problem
differences = np.abs(left_sorted - right_sorted)
total_distance = np.sum(differences)
print("🛷 Total mismatch distance:", total_distance)


# second problem
right_counts = Counter(right_list)
similarity_score = sum(num * right_counts[num] for num in left_list)
print("🎅 Similarity score:", similarity_score)

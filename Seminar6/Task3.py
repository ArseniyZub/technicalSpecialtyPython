import random

def generate_placement(size):
    queens_placement = []

    for _ in range(size):
        column = random.randint(0, size - 1)
        queens_placement.append(column)

    return queens_placement

def is_safe(queens_placement):
    size = len(queens_placement)

    for i in range(size):
        for j in range(i + 1, size):
            if queens_placement[i] == queens_placement[j] or abs(queens_placement[i] - queens_placement[j]) == abs(i - j):
                return False

    return True

def find_safe_queens_placements(size, num_placements):
    safe_placements = []

    while len(safe_placements) < num_placements:
        queens_placement = generate_placement(size)

        if is_safe(queens_placement):
            safe_placements.append(queens_placement)

    return safe_placements


size = 8  
num_placements_to_find = 4 

safe_placements = find_safe_queens_placements(size, num_placements_to_find)

for i, placement in enumerate(safe_placements):
    print(f"Размещение {i + 1}: {placement}")

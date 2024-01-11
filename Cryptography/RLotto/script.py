import random
import time

def find_seed(to_find):
    for seed in range(1704000000, 1705000000):  # Example range, adjust as needed
        random.seed(seed)
        extracted = [random.randint(1, 90) for _ in range(len(to_find))]
        if extracted == to_find:
            return seed
    return None

to_find = [69, 83, 35, 68, 52]
seed = find_seed(to_find)
if seed is not None:
    print(f"Seed found: {seed}")
    next_extraction = [random.randint(1, 90) for _ in range(5)]
    print(f"Next extraction: {next_extraction}")
else:
    print("Seed not found in the given range.")

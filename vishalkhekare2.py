#2. Task 9: Calculate mean, median, and mode of a dataset

import statistics

def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    return mean, median, mode

# Example Usage:
data = [1, 2, 2, 3, 4]
mean, median, mode = calculate_statistics(data)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

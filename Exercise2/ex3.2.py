import json
import time
import random
import matplotlib.pyplot as plt

# Load the input array from ex2data.json
with open('Exercise2/ex2data.json', 'r') as f:
    input_array = json.load(f)

# Load the list of search tasks from ex2tasks.json
with open('Exercise2/ex2tasks.json', 'r') as f:
    search_tasks = json.load(f)


def binary_search(arr, target, start, end, mid):
    # Use the provided initial midpoint for the first iteration
    if start == 0 and end == len(arr) - 1:
        mid = start + (end - start) // 2

    while start <= end:
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

        mid = start + (end - start) // 2

    return -1


# Perform binary search for each search task using random midpoints
results = []
for task in search_tasks:
    min_time = float('inf')
    best_mid = -1
    for i in range(10):
        mid = random.randint(0, len(input_array) - 1)
        start = 0
        end = len(input_array) - 1
        start_time = time.time()
        result = binary_search(input_array, task, start, end, mid)
        end_time = time.time()
        search_time = end_time - start_time
        if search_time < min_time:
            min_time = search_time
            best_mid = mid
    results.append((task, best_mid, min_time))

# Plot the best midpoints for each search task
search_tasks = []
best_midpoints = []
for result in results:
    search_tasks.append(result[0])
    best_midpoints.append(result[1])

plt.scatter(search_tasks, best_midpoints)
plt.xlabel('Search Task')
plt.ylabel('Best Midpoint')
plt.title('Best Midpoint for Each Search Task')
plt.show()

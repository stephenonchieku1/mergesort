import random
import time
import matplotlib.pyplot as plt
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_sorting_time(n: int) -> float:
    # Generate random numbers
    arr = [random.randint(1, 10000) for _ in range(n)]
    
    # Measure time
    start_time = time.time()
    merge_sort(arr.copy())  
    end_time = time.time()
    
    return end_time - start_time

def run_experiment():
    # Test with different array sizes
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
    times = []
    
    # Run sorting for each size
    for size in sizes:
        time_taken = measure_sorting_time(size)
        times.append(time_taken)
        print(f"Time taken to sort {size} elements: {time_taken:.4f} seconds")
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'b-o')
    plt.title('Merge Sort Performance Analysis')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.grid(True)
    plt.show()

    # Save results to file
    with open('sorting_results.txt', 'w') as f:
        f.write("Merge Sort Performance Results\n")
        f.write("-----------------------------\n")
        for size, time_taken in zip(sizes, times):
            f.write(f"n = {size}: {time_taken:.4f} seconds\n")

if __name__ == "__main__":
    run_experiment()
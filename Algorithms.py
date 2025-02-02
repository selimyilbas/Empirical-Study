import random
import time
import pandas as pd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def improved_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi-1)
        quick_sort_helper(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def improved_quick_sort(arr):
    if len(arr) < 20:
        selection_sort(arr)
    else:
        quick_sort_helper(arr, 0, len(arr) - 1)

def generate_random_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

def run_and_measure(sort_function, data, sort_name, size):
    times = []
    for i in range(5):
        data_copy = data.copy()
        time_taken = measure_time(sort_function, data_copy)
        times.append(time_taken)
        print(f"{i+1}st run sorted {size} elements in {time_taken:.6f} seconds")
    average_time = sum(times) / len(times)
    print(f"Average time for {sort_name} with {size} elements: {average_time:.6f} seconds\n")
    return average_time

if __name__ == "__main__":
    input_sizes = [100, 1000, 10000, 100000]
    results = []

    for size in input_sizes:
        data = generate_random_data(size)
        results.append({
            "Input Size": size,
            "BubbleSort": run_and_measure(bubble_sort, data, "BubbleSort", size),
            "SelectionSort": run_and_measure(selection_sort, data, "SelectionSort", size),
            "QuickSort": run_and_measure(lambda arr: quick_sort(arr.copy()), data, "QuickSort", size),
            "MergeSort": run_and_measure(merge_sort, data, "MergeSort", size),
            "ImprovedBubbleSort": run_and_measure(improved_bubble_sort, data, "ImprovedBubbleSort", size),
            "ImprovedQuickSort": run_and_measure(improved_quick_sort, data, "ImprovedQuickSort", size)
        })

    df = pd.DataFrame(results)
    df.to_excel("sorting_algorithms_performance.xlsx", index=False)

    print("Results saved to sorting_algorithms_performance.xlsx")

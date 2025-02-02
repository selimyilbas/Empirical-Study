# Empirical Study on Sorting Algorithms

This project is a detailed empirical study comparing the performance of six sorting algorithms implemented in Python. The study evaluates their execution times 
for varying input sizes and produces an Excel file and a performance comparison chart. The project also includes a video demonstration.

## Project Description
The study includes the following sorting algorithms:

***Bubble Sort:*** A basic sorting algorithm that compares adjacent elements and swaps them if they are in the wrong order.

***Selection Sort:*** Finds the smallest element and swaps it with the first unsorted element.

***Quick Sort:*** A divide-and-conquer algorithm that partitions an array into smaller sub-arrays.

***Merge Sort:*** A stable sorting algorithm that recursively divides the array into halves and merges sorted halves.

***Improved Bubble Sort:*** A more optimized version of Bubble Sort with an early exit mechanism.

***Improved Quick Sort:*** Combines Quick Sort with Selection Sort for small input sizes to enhance performance.


## Features
***Performance Analysis:*** Measures execution times for different input sizes.

***Excel Output:*** Saves results in an Excel file for further analysis.

***Chart Visualization:*** Creates a line chart comparing execution times of the algorithms.

***Video Demonstration:*** Includes a video showcasing the sorting process and results.

![Algoritthms](https://github.com/user-attachments/assets/6309a873-a13f-474a-a31e-75ba6a508cd8)


## How to Run the Project
# 1. Clone the Repository
Open a terminal and run:

```
git clone https://github.com/selimyilbas/Empirical-Study.git
cd Empirical-Study
```

# 2. Install Dependencies
Make sure you have Python installed. Then, install the required library:

```
pip install pandas

```

# 3. Run the Script
Run the main Python script to measure execution times and generate results:

```
python algorithms.py
```


# Expected Output

Console Output:
Execution times for each algorithm and input size are printed.

```
BubbleSort:
1st run sorted 100 elements in 0.002134 seconds
2nd run sorted 100 elements in 0.001947 seconds
Average time for BubbleSort with 100 elements: 0.002041 seconds
```


# Auto Generated Files:

***sorting_algorithms_performance.xlsx***: Contains execution times for all algorithms.

***line_chart.png***: A performance comparison chart.






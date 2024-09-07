# Algorithm Analysis and Implementation

## Overview

This repository contains an analysis of the time complexity for a given algorithm, a modified version of the algorithm, and an implementation of merge sort. The analysis includes runtime measurements, polynomial fitting, and Big-O notation determination.

## Table of Contents

1. [Function Analysis](#function-analysis)
2. [Runtime Measurement and Plotting](#runtime-measurement-and-plotting)
3. [Curve Fitting and Polynomial Bounds](#curve-fitting-and-polynomial-bounds)
4. [Effect of Modifications](#effect-of-modifications)
5. [Merge Sort Implementation](#merge-sort-implementation)

## Function Analysis

The initial function to analyze is:

```matlab
function x = f(n)
   x = 1;
   for i = 1:n
        for j = 1:n
             x = x + 1;
```

### Runtime Analysis

- **Algorithm Complexity:**

  The time complexity can be determined by analyzing the number of operations performed:

  \[
  \text{Total Operations} = \sum_{i=1}^{n} \sum_{j=1}^{n} 1 = n \cdot n = n^2
  \]

  Thus, the runtime of the algorithm is \(O(n^2)\).

## Runtime Measurement and Plotting

The function was timed for various values of \( n \) (from 1 to 1000) and plotted to visualize the relationship between execution time and \( n \).

### Code for Timing and Plotting

```python
import time
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

n_values = list(range(1, 1001))
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(n_values, times, label='Time vs n')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Function f(n)')
plt.show()
```

## Curve Fitting and Polynomial Bounds

A polynomial curve (degree 2) was fitted to the timing data to confirm the \(O(n^2)\) complexity.

### Code for Curve Fitting

```python
coeffs = np.polyfit(n_values, times, 2)
p = np.poly1d(coeffs)

plt.plot(n_values, times, label='Time vs n')
plt.plot(n_values, p(n_values), label='Fitted Curve (Degree 2)', linestyle='--')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Function f(n) with Fitted Curve')
plt.legend()
plt.show()
```

### Big-O, Big-Omega, and Big-Theta

- **Big-O (Upper Bound):** \(O(n^2)\)
- **Big-Omega (Lower Bound):** \(\Omega(n^2)\)
- **Big-Theta:** \(\Theta(n^2)\)

## Effect of Modifications

### Modified Function

```matlab
function x = f(n)
   x = 1;
   y = 1;
   for i = 1:n
        for j = 1:n
             x = x + 1;
             y = i + j;
```

- **Impact on Runtime:** The additional line `y = i + j;` does not significantly change the overall runtime complexity. The function remains \(O(n^2)\).
- **Effect on Results:** The asymptotic complexity remains \(O(n^2)\), so the results from the initial analysis are unaffected.

## Merge Sort Implementation

### Code for Merge Sort

```python
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

test_array = [5, 2, 4, 7, 1, 3, 2, 6]
merge_sort(test_array)
print("Sorted array is:", test_array)
```

### Testing Merge Sort

The provided code sorts the array `[5, 2, 4, 7, 1, 3, 2, 6]` and outputs the sorted result.

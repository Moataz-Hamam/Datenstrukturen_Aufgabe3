# Search Algorithm Benchmark

## Overview

This program compares the performance of four different search algorithms:

* Linear Search
* Binary Search
* Interpolation Search
* Quad Search

The algorithms are tested on different types of sorted arrays and their execution times are measured.

---

# Search Algorithms

## Linear Search

Linear Search checks each element of the array one by one until the target value is found.

### Steps

1. Start at the first element.
2. Compare the current element with the target.
3. If they match, return the index.
4. Otherwise continue with the next element.
5. If the end of the array is reached, return `-1`.

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Average | O(n)       |
| Worst   | O(n)       |

---

## Binary Search

Binary Search works only on sorted arrays.

Instead of checking every element, it repeatedly divides the search interval into two halves.

### Steps

1. Select the middle element.
2. Compare it with the target.
3. If equal, return the index.
4. If the target is larger, search the right half.
5. If the target is smaller, search the left half.
6. Repeat until the element is found or the interval becomes empty.

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Average | O(log n)   |
| Worst   | O(log n)   |

---

## Interpolation Search

Interpolation Search is an improved version of Binary Search for uniformly distributed data.

Instead of always choosing the middle element, it estimates where the target is likely located.

### Steps

1. Calculate an estimated position using interpolation.
2. Compare the value at that position with the target.
3. Adjust the search range.
4. Repeat until the target is found or the search interval becomes invalid.

### Time Complexity

| Case    | Complexity   |
| ------- | ------------ |
| Best    | O(1)         |
| Average | O(log log n) |
| Worst   | O(n)         |

---

## Quad Search

Quad Search combines ideas from Interpolation Search and Jump Search.

It first estimates the target position and then moves through the array in larger steps based on the square root of the current search range.

### Steps

1. Estimate the probable target position.
2. Compare the value at that position.
3. Move left or right using jump steps.
4. Recursively search inside the reduced interval.
5. Repeat until the target is found or no valid interval remains.

### Time Complexity

| Case    | Complexity                                      |
| ------- | ----------------------------------------------- |
| Best    | O(1)                                            |
| Average | Better than Binary Search on some distributions |
| Worst   | O(n)                                            |

---

# Test Arrays

The benchmark uses three different array types.

## Linear Array

Values grow approximately linearly.

Example:

```text
[0.1, 1.0, 2.2, 3.1, 4.0, 5.2]
```

Characteristics:

* Nearly uniform distribution
* Ideal for Interpolation Search

---

## Random Sorted Array

Random values are generated and then sorted.

Example:

```text
[0.3, 2.7, 4.9, 8.5, 13.1]
```

Characteristics:

* Non uniform distribution
* More realistic dataset

---

## Worst-Case Array

The array grows normally except for the last value, which is extremely large.

Example:

```text
[0, 1, 2, 3, 4, 5, 1000000]
```

Characteristics:

* Creates unfavorable conditions for Interpolation Search
* Demonstrates worst case behavior

---

# Performance Measurement

Execution times are measured using:

```python
time.perf_counter()
```

For each test:

1. The search algorithm is executed multiple times.
2. The minimum measured runtime is selected.
3. Results are displayed in microseconds (µs).

This approach reduces the impact of operating system scheduling and background processes.

---

# Benchmark Configuration

Array sizes used:

```python
[1000, 5000, 20000, 100000]
```

Search target:

```python
arr[n // 2]
```

The middle element of the array is chosen to provide consistent benchmark results.

---

# Conclusion

The benchmark demonstrates the strengths and weaknesses of different search algorithms.

* Linear Search is simple but inefficient for large datasets.
* Binary Search provides reliable logarithmic performance.
* Interpolation Search performs extremely well on uniformly distributed data but can degrade to linear complexity in unfavorable cases.
* Quad Search attempts to improve interpolation-based searching by combining estimation and jump-based narrowing of the search interval.

The results show how data distribution can significantly influence search performance and why selecting an appropriate algorithm depends on the characteristics of the dataset.
# Datenstrukturen_Aufgabe3

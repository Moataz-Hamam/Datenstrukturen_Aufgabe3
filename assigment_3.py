import math
import time
import numpy as np


# --------------------------------------------------
# Search Algorithms
# --------------------------------------------------

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def interpolation_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:

        if arr[left] == arr[right]:
            return left if arr[left] == target else -1

        pos = left + int(
            (right - left)
            * (target - arr[left])
            / (arr[right] - arr[left])
        )

        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1


def quad_search(arr, target):

    def helper(left, right):

        if left > right:
            return -1

        size = right - left + 1

        if arr[left] == arr[right]:
            return left if arr[left] == target else -1

        pos = left + int(
            (right - left)
            * (target - arr[left])
            / (arr[right] - arr[left])
        )

        if arr[pos] == target:
            return pos

        step = int(math.sqrt(size))

        if target < arr[pos]:

            while pos > left and target < arr[pos]:
                pos -= step

            return helper(
                max(left, pos),
                min(right, pos + step)
            )

        else:

            while pos < right and target > arr[pos]:
                pos += step

            return helper(
                max(left, pos - step),
                min(right, pos)
            )

    return helper(0, len(arr) - 1)


# --------------------------------------------------
# Array Generators
# --------------------------------------------------

def make_linear_array(n):
    rng = np.random.default_rng()
    return np.sort(
        np.arange(n) + rng.uniform(-0.4, 0.4, n)
    )


def make_random_sorted_array(n):
    rng = np.random.default_rng()
    return np.sort(
        rng.uniform(0, 2 * n, n)
    )


def make_worst_case_array(n):
    return np.array(
        list(range(n - 1)) + [n * n],
        dtype=float
    )


# --------------------------------------------------
# Timing
# --------------------------------------------------

def measure_time(search_fn, arr, target, repeats=5):

    best = float("inf")

    for _ in range(repeats):
        start = time.perf_counter()

        search_fn(arr, target)

        elapsed = time.perf_counter() - start

        best = min(best, elapsed)

    return best


# --------------------------------------------------
# Main Program
# --------------------------------------------------

if __name__ == "__main__":

    algorithms = [
        linear_search,
        binary_search,
        interpolation_search,
        quad_search
    ]

    arrays = {
        "Linear": make_linear_array,
        "Random": make_random_sorted_array,
        "Worst": make_worst_case_array
    }

    sizes = [1000, 5000, 20000, 100000]

    for array_name, generator in arrays.items():

        print(f"\n--- {array_name} Array ---")

        for algo in algorithms:

            print(f"\n{algo.__name__}")

            for n in sizes:

                arr = generator(n)
                target = arr[n // 2]

                t = measure_time(algo, arr, target)

                print(
                    f"n={n:<6} -> {t * 1e6:.2f} µs"
                )
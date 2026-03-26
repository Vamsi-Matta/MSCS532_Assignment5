import random
import time


def quicksort_fixed(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]  

    left_partition = [value for value in arr if value < pivot]
    middle_partition = [value for value in arr if value == pivot]
    right_partition = [value for value in arr if value > pivot]

    return (
        quicksort_fixed(left_partition)
        + middle_partition
        + quicksort_fixed(right_partition)
    )


def quicksort_random(arr):
    if len(arr) < 2:
        return arr

    pivot = random.choice(arr)

    left_partition = [value for value in arr if value < pivot]
    middle_partition = [value for value in arr if value == pivot]
    right_partition = [value for value in arr if value > pivot]

    return (
        quicksort_random(left_partition)
        + middle_partition
        + quicksort_random(right_partition)
    )


def generate_input(size, order_type):
    if order_type == "random":
        return random.sample(range(size * 10), size)
    elif order_type == "sorted":
        return list(range(size))
    elif order_type == "reversed":
        return list(range(size, 0, -1))
    return []


def measure_execution_time(sort_function, data):
    start_time = time.perf_counter()
    sort_function(data.copy())
    end_time = time.perf_counter()
    return round((end_time - start_time) * 1000, 3)


def run_experiment():
    input_sizes = [100, 1000, 3000]
    input_types = ["random", "sorted", "reversed"]

    print("Quicksort Performance Results (in milliseconds)\n")

    for input_type in input_types:
        print(f"Input Type: {input_type}")
        for size in input_sizes:
            dataset = generate_input(size, input_type)

            fixed_time = measure_execution_time(quicksort_fixed, dataset)
            random_time = measure_execution_time(quicksort_random, dataset)

            print(
                f"Size {size}: Fixed Pivot = {fixed_time} ms | "
                f"Random Pivot = {random_time} ms"
            )
        print()


if __name__ == "__main__":
    run_experiment()
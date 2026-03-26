import random


def quick_sort_random(values):
    if len(values) < 2:
        return values

    pivot = random.choice(values)

    lower_part = [item for item in values if item < pivot]
    equal_part = [item for item in values if item == pivot]
    higher_part = [item for item in values if item > pivot]

    return quick_sort_random(lower_part) + equal_part + quick_sort_random(higher_part)


if __name__ == "__main__":
    sample_values = [9, 4, 6, 2, 8, 1, 5]
    sorted_values = quick_sort_random(sample_values)
    print("Sorted output using randomized Quicksort:")
    print(sorted_values)

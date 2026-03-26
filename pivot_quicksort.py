def sort_data(data):
    if len(data) < 2:
        return data

    pivot = data[0]
    smaller = [value for value in data[1:] if value <= pivot]
    greater = [value for value in data[1:] if value > pivot]

    return sort_data(smaller) + [pivot] + sort_data(greater)


if __name__ == "__main__":
    sample_values = [9, 4, 6, 2, 8, 1, 5]
    sorted_values = sort_data(sample_values)
    print("Sorted output using fixed pivot Quicksort:")
    print(sorted_values)

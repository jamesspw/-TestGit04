def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def merge_sort_with_steps(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_with_steps(left_half)
    right_half = merge_sort_with_steps(right_half)

    print("Merging:", left_half, right_half)
    merged_result = merge(left_half, right_half)
    print("Merged:", merged_result)

    return merged_result


if __name__ == "__main__":
    input_list = [3, 5, 8, 6, 7, 4, 1, 2, 9]
    print("Original Array:", input_list, '\n')

    sorted_array = merge_sort_with_steps(input_list)
    print("\nFinal Sorted Array:", sorted_array)

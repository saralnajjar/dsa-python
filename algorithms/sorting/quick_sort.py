def quick_sort(arr):
    arr = arr.copy()
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, low, high):
    if low < high:
        pivot_index = _partition(arr, low, high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    # Median-of-three pivot selection
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    pivot = arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]  # move pivot to end

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print(f"Input:  {test}")
    print(f"Sorted: {quick_sort(test)}")

    # Edge cases
    print(quick_sort([]))        # []
    print(quick_sort([1]))       # [1]
    print(quick_sort([2, 1]))    # [1, 2]
    print(quick_sort([1, 1, 1])) # [1, 1, 1]
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break  # early exit if already sorted

    return arr


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print(f"Input:  {test}")
    print(f"Sorted: {bubble_sort(test)}")

    # Edge cases
    print(bubble_sort([]))        # []
    print(bubble_sort([1]))       # [1]
    print(bubble_sort([2, 1]))    # [1, 2]
    print(bubble_sort([1, 1, 1])) # [1, 1, 1]
def bisect_left(arr, target):
    """
    Locate the insertion point for `target` in `arr` to maintain sorted order.
    If `target` is already present, returns the index of the first occurrence.

    :param arr: Sorted list of elements.
    :param target: The target value to locate.
    :return: The index of the first occurrence or the insert position.
    """
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:  # Target is on the right
            low = mid + 1
        else:  # Target is on the left or at mid
            high = mid-1

    return low


def bisect_right(arr, target):
    """
    Locate the insertion point for `target` in `arr` to maintain sorted order.
    If `target` is already present, returns the index after the last occurrence.

    :param arr: Sorted list of elements.
    :param target: The target value to locate.
    :return: The index after the last occurrence or the insert position.
    """
    low, high = 0, len(arr)

    low, high = 0, len(arr) - 1
    result = -1  # To track the last occurrence

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:  # Target is on the right or at mid
            if arr[mid] == target:
                result = mid  # Update last occurrence
            low = mid + 1  # Move right
        else:  # Target is on the left
            high = mid - 1

    return result if result != -1 else low


arr = [1, 3, 3, 5, 7, 9]
target = 10
lower = bisect_left(arr, target)
print(f"bisect_left({target}): {lower}")  
upper = bisect_right(arr, target)
print(f"bisect_right({target}): {upper}")

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        md = (right + left) // 2
        if arr[md] > target:
            right = md - 1
        elif arr[md] < target:
            left = md + 1
        else:
            return md
    print("Value not present")
    return -1

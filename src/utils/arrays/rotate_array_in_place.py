def rotate(arr, k):
    length = len(arr)
    k %= length

    start = count = 0

    while count < length:
        current, previous = start, arr[start]
        while True:
            # if k > length, take remainder and move that many steps
            next_i = (current + k) % length
            # make next step of k, rotating values
            arr[next_i], previous = previous, arr[next_i]
            # set current index to next index
            current = next_i
            # increment to base case of reaching last index
            count += 1

            if start == current:
                break
            # perform next iteration of replacement cycle on following index
            # (e.g. with length = 4 and k = 2, this would move from start = 0 -> start = 1)
        start += 1


# Helper function that reverses elements between given indices in an array. implemented in method 2
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1


def rotate_method_2(arr, k):
    n = len(arr)
    k %= n

    # reverse entire array
    reverse(arr, 0, n - 1)
    # flip first portion back
    reverse(arr, 0, k - 1)
    # flip end
    reverse(arr, k, n - 1)


test_arr = [0, 1, 2, 3, 4, 5]
rotate(test_arr, 2)
print("After method 1:", test_arr)
rotate_method_2(test_arr, -2)
print("After method 2:", test_arr)
# Should return:
# [4, 5, 0, 1, 2, 3]
# [0, 1, 2, 3, 4, 5]

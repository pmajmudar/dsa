

arr = [4, 8, 10, 23, 12, 45, 2, 5, 7, 9]

arr = sorted(arr)


def binary_search(array, target, start, end):
    """Recursive binary search.

    Array - sorted array to search
    Target - value to find
    start - start index of array
    end - end index of array.
    """
    if not array or end == len(array) or start == len(array):
        return -1

    mid_index = (start + end) // 2
    print("Mid:", mid_index, "target: ", target, "start: ", start, "end: ", end, "array: ", array)
    mid_val = array[mid_index]
    if mid_val == target:
        print(mid_val)
        return mid_index
    elif target > mid_val:
        ans = binary_search(array, target, mid_index + 1, end)
    else:
        ans = binary_search(array, target, start, mid_index - 1)
    return ans

res = binary_search(arr, 23, 0, len(arr) - 1)
print("Index found: ", res)

res = binary_search(arr, 45, 0, len(arr) - 1)
print("Index found: ", res)

res = binary_search(arr, 10, 0, len(arr) - 1)
print("Index found: ", res)

def binary_search_it(array, val):
    if not array:
        return
    # assign left / right pointers
    left = 0
    right = len(array) - 1

    # continue search until left less than equal to right
    while left <= right:
        # calculate mid-pt
        mid = (left + right) // 2
        print(left, right, val, mid, array[mid])
        if array[mid] == val:
            return True
        elif array[mid] < val:
            left = mid + 1
        elif array[mid] > val:
            right = mid - 1
    return False

print("Iterative search")
binary_search_it(arr, 23)

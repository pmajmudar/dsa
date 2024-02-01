

arr = [4, 8, 10, 23, 12, 45, 2, 5, 7, 9]

arr = sorted(arr)


def binary_search(array, val):
    if not array:
        return
    mid = len(array) // 2
    print("Mid:", mid, "array: ", array)
    mid_val = array[mid]
    if val == mid_val:
        print(mid_val)
        return True
    elif len(array) == 1:
        return False
    elif val > mid_val:
        ans = binary_search(array[mid:], val)
    else:
        ans = binary_search(array[:mid], val)
    return ans

res = binary_search(arr, 23)
print(res)

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

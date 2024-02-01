
def partition2(arr, low, high):
    i = low
    pivot = arr[high]
    print("Partiton: ", i, low, high, pivot)

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j],arr[i] = arr[i],arr[j]
            i += 1
    arr[i],arr[high] = arr[high], arr[i]
    #print(arr)
    return i

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    print("Partiton: ", i, low, high, pivot)

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    #print(arr)
    return i+1


def qsort(arr, low, high):
    if low >= high:
        print("Exiting low: ", low, " high: ", high)
        return
    print("Pre: ", low, ", ", high, ", ", arr)
    pivot_idx = partition2(arr, low, high)
    print("Post: ", low, ", ", high, ", ", arr)
    qsort(arr, low, pivot_idx - 1)
    qsort(arr, pivot_idx + 1, high)


arr = [2, 3, 8, 9, 5, 4, 2, 6, 7]
#print(arr)
qsort(arr, 0, len(arr) - 1)
print("END")
print(arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def find_min_rec(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        minNumber = find_min_rec(arr[1:])
        min_value = arr[0]
        print(min_value, minNumber)

        if minNumber < min_value:
            min_value = minNumber
        return min_value


if __name__ == "__main__":
    arr = [4, 2, 1, 8]
    # print(selection_sort(arr))
    print(find_min_rec(arr))

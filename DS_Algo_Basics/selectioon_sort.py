def selection_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n):
        min_val = arr[i]
        min_index = i
        for j in range(i+1, n):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
        

if __name__ == '__main__':
    a = [6, 5, 4, 3, 2, 1]
    print(selection_sort(a))



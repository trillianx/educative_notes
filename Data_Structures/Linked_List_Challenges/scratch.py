def selection_sort(arr):
    # Traverse through all the array elements:
    for index, value in enumerate(arr):
        min_index = index
        for ind, val in enumerate(min_index+1, arr):
            if val < value:
                min_index = ind
        
        # Swap the found minimum element with the first element
        arr[index], arr[min_index] = arr[min_index], arr[ind]
        print(arr)
        

if __name__ == "__main__":
    arr = [8, 5, 2, 6, 9, 3, 1, 4, 8, 7]
    selection_sort(arr)
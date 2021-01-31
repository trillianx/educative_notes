def sort_array(arr, length):
    if length == 0:
        return
    else:
        sort_array(arr[1:], length-1)
        arr.insert(arr[0],0)

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    sort_array(arr, 5)
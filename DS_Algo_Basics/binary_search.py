def binary_search(arr, element):
    if len(arr) == 0:
        return False
    else:
        middle_index = len(arr) // 2
        left = arr[:middle_index]
        right = arr[middle_index+1:]
        if element == arr[middle_index]:
            return True
        elif element < arr[middle_index]:
            return binary_search(left, element)
        else:
            return binary_search(right, element)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    result = binary_search(arr, 6)
    print(result)
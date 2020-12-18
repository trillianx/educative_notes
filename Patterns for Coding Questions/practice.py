def remove_duplicates(arr):
    non_dup_index = 1
    index = 1
    while index < len(arr):
        if arr[non_dup_index - 1] != arr[index]:
            arr[non_dup_index] = arr[index]
            non_dup_index += 1
        index += 1
    return arr[:non_dup_index] 


if __name__ == "__main__":
    arr = arr = [2, 3, 3, 3, 6, 9, 9]
    arr2 = [2, 5, 9, 11]
    target = 6
    print(remove_duplicates(arr))
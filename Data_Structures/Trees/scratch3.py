def count_sort(arr):
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    output = [0] * len(arr)
    for i in arr:
        count_arr[i] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] = count_arr[i-1] + count_arr[i]
    # print(count_arr)
    for i in arr:
        count_loc = count_arr[i]
        new_index = count_loc - 1
        output[new_index] = i
        count_arr[i] -= 1
    
    return output

if __name__ == "__main__":
    arr = [652, 0, 999, 1111, 7, 432, 10000]
    print(arr)
    result = count_sort(arr)
    print(result)
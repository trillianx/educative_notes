def max_sub(k, arr):
    sum_val = 0
    start = 0
    max_val = 0
    for end in range(len(arr)):
        sum_val += arr[end]
        if end >= k - 1:
            max_val = max(max_val, sum_val)
            sum_val = sum_val - arr[start]
            start += 1
    return max_val
if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    arr2 = [2, 3, 4, 1, 5]
    k = 2
    print(max_sub(k, arr2))
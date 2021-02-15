import numpy as np
def small_window(arr, S):
    n = len(arr)
    max_val = []
    for start in range(n):
        sums = arr[start]
        end = 0
        while start + end < n and sums <= S:
            sums += arr[end]
            end += 1
        max_val.append(end)
    return max_val


if __name__=='__main__':
    arr = [2, 1, 5, 2, 3, 2]
    S = 7 
    print(small_window(arr, S))
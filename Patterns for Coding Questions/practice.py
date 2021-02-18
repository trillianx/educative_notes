def square(arr):
    n = len(arr)
    start = 0
    end = n - 1
    index = end
    sq = [0] * n
    while start <= end:
        sn = arr[start] ** 2
        en = arr[end] ** 2
        if sn > en:
            sq[index] = sn
            start += 1
        else:
            sq[index] = en
            end -= 1
        index -= 1
    return sq



if __name__ == '__main__':
    arr = [-2, -1, 0, 2, 3]
    arr2 = [-3, -1, 0, 1, 2]
    print(arr)
    print("")
    print(square(arr))
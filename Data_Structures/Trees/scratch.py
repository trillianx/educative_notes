def find_val(arr, value):
    n = len(arr)
    if n == 0:
        return 0
    count = 0
    for e in arr:
        if e == value:
            count += 1
    return count

def find_valr(arr, value, count):
    if len(arr) == 0:
        return count
    else:
        if arr[0] == value:
            count = find_valr(arr[1:], value, count+1)
        else:
            count = find_valr(arr[1:], value, count)
    return count

def find_length(arr, count):
    if arr == []:
        return count
    else:
        count = find_length(arr[1:], count+1)
    return count
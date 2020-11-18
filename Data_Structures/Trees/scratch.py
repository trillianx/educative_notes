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


def find_length(arr):
    if arr == []:
        return 0
    else:
        return 1 + find_length(arr[1:])

def reverse(arr):
    if len(arr) == 0:
        return []
    else:
        return reverse(arr[1:]) + [arr[0]]

def replace(arr):
    if len(arr) == 0:
        return []
    else:
        if arr[0] < 0:
            return [0] + replace(arr[1:])
        else:
            return [arr[0]] + replace(arr[1:])


def find_sum(arr, currentIndex):
    if currentIndex == len(arr) - 1:
        return arr[currentIndex]
    
    if currentIndex == 0:
        return ((arr[currentIndex] + find_sum(arr, currentIndex + 1)) / len(arr))
    
    return (arr[currentIndex] + find_sum(arr, currentIndex + 1))

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(find_sum(arr, 0))


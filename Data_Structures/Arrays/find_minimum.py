def find_minimum(lst):
    start = 0
    end = len(lst) - 1
    while start < end: 
        if lst[start] < lst[end]:
            end -= 1
        else:
            start += 1
    return lst[start]

if __name__ == "__main__":
    arr = [9, 2, 3, 6]
    print(find_minimum(arr))
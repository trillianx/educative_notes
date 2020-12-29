def rearrange(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        while lst[start] < 0 and start < end:
            start += 1
        while lst[end] > 0 and start < end:
            end -= 1
        if start < end:
            lst[start], lst[end] = lst[end], lst[start]
    return lst

if __name__ == "__main__":
    arr = [10,-1,20,4,5,-9,-6,-2,-5,10,20,-30]
    print(rearrange(arr))
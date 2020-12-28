def find_sum(lst, k):
    lst.sort()
    start = 0
    end = len(lst) - 1
    while start < end: 
        sum = lst[start] + lst[end]
        if sum == k: 
            return [lst[start], lst[end]]
        elif sum > k: 
            end -= 1
        elif sum < k:
            start += 1
    if start < end:
        return [lst[start], lst[end]]
    else:
        return -1

if __name__ == "__main__":
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    print(find_sum(lst, k))


def right_rotate(lst, k):
    if len(lst) < 2:
        return lst
    if k > len(lst):
        return None
    index = k - 1
    return lst[index:] + lst[:index]

if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50]
    lst = [0, 0, 0, 2]
    k = 2
    print(right_rotate(lst, k))
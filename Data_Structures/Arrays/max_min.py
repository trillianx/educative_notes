def maxMin(lst):
    if len(lst) < 2:
        return None
    left = 0
    right = len(lst) - 1
    result = []
    while left < right:
        result.append(lst[right])
        result.append(lst[left])
        left += 1
        right -= 1
    print(left, right)
    if left == right:
        return result + [lst[left]]
    else:
        return result

if __name__ == "__main__":
    # lst = [-10, -1, 1, 1, 1, 1]
    lst = [1, 2, 3, 4, 5, 6]
    print(maxMin(lst))
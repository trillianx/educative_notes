def merge_lst(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    l1 = 0
    l2 = 0
    while l1 < n1 and l2 < n2:
        # if the current element in lst1 is
        # greater than the current element in lst2
        if lst1[l1] > lst2[l2]:
            # Insert lst2 element in lst2 at l1 index
            lst1.insert(l1, lst2[l2])
            l1 += 1
            l2 += 1
        else:
            l1 += 1

    return lst1 + lst2[l2:]

if __name__ == "__main__":
    lst1 = [1, 30, 40, 50]
    lst2 = [2, 6, 7, 8, 9]
    result = merge_lst(lst1, lst2)
    print(result)
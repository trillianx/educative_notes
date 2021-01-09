def is_subset(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    result = s1.intersection(s2)
    if len(result) == len(lst2):
        return True
    else:
        return False

if __name__ == "__main__":
    list1 = [9, 4, 7, 1, -2, 6, 5]
    list2 = [7, 1, -2]
    list3 = [10, 12]
    print(is_subset(list1, list2))
    print(is_subset(list1, list3))
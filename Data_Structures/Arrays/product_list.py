def find_product(lst):
    n = len(lst)
    result = []
    for i in range(n):
        if i < n:
            sublist = lst[0:i] + lst[i+1:]
            prod = 1
            for e in sublist:
                prod = prod * e
            result.append(prod)
    return result
        

if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(find_product(lst))
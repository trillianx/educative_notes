def binary_search_iterations(num):
    if num // 2 == 1:
        return 1
    else:
        return 1 + binary_search_iterations(num // 2)

if __name__ == '__main__':
    num = 16
    print(binary_search_iterations(num))
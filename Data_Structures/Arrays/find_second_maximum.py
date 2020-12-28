import numpy as np

def find_second_max(lst):
    if len(lst) < 2:
        return None
    first_max = float('-inf')
    second_max = float('-inf')
    for i in range(len(lst)):
        if lst[i] > first_max:
            second_max = first_max
            first_max = lst[i]
        elif lst[i] < first_max and lst[i] > second_max:
            second_max = lst[i]
    
    if not second_max == float('-inf'):
        return second_max
    else:
        return None

if __name__ == "__main__":
    arr = [1, 2, 4, 3, 3, 5]
    print(find_second_max(arr))


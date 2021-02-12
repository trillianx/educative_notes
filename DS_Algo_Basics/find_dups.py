def find_dups(arr):
    n = len(arr)
    if n <= 1:
        return False
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j] and i != j:
                return True
    return False

def find_dups_linear(arr):
    unique_vals = []
    for e in arr:
        if e not in unique_vals:
            unique_vals.append(e)
        else:
            return True
    return False

if __name__ == '__main__':
    a = [1, 5, 3, 9, 1, 4]
    print(find_dups_linear(a))
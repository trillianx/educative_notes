def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(lst1, lst2):
    output = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            output.append(lst1[i])
            i += 1
        else:
            output.append(lst2[j])
            j += 1
    output = output + lst1[i:] + lst2[j:]
    return output

if __name__ == "__main__":
    arr1 = [1, 5, 8, 15, 24]
    arr2 = [3, 10, 16, 20]
    arr = [15, 5, 24, 8, 1, 3, 16, 10, 20]
    #result = merge(arr1, arr2)
    result = merge_sort(arr)
    print(result)
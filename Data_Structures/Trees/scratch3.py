def QuickSort(arr):

    n = len(arr)
    
    #Base case
    if n < 2:
        return arr
    
    #Position of the partitioning element
    pivot = arr[0]
    frontier = 0 

    #Partitioning loop
    for i in range(1, n): 
         if arr[i] <= pivot:
              frontier += 1
              # Now swap the values
              arr[i], arr[frontier] = arr[frontier], arr[i]

    arr[0], arr[frontier] = arr[frontier], arr[0]
    print(frontier)

  
    #Sorts the elements to the left of pivot
    left = QuickSort(arr[0:frontier])
    
    #sorts the elements to the right of pivot
    right = QuickSort(arr[frontier+1:n]) 

    #Merging everything together
    arr = left + [arr[frontier]] + right 
    
    return arr

if __name__ == "__main__":
    arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
    result = QuickSort(arr)
    print(result)
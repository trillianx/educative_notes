def remove_evens(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:

        # Move left index until you find an odd value: 
        while lst[left] % 2 == 0 and left < right:
            left += 1

        # Move right index until you find an even value: 
        while lst[right] % 2 != 0 and left < right:
            right -= 1

        # Once found, we swap even and odd: 
        if left < right: 
            lst[left], lst[right] = lst[right], lst[left]

    print(lst)
    # We return the desired subarray: 
    return lst[left:]


if __name__ == "__main__":
    arr = [12, 34, 45, 9, 8, 90, 3]
    print(remove_evens(arr))
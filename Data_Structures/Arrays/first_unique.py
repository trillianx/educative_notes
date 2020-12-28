def find_first_unique(lst):
    for i in range(len(lst)):
        end = 0
        while end < len(lst):
            if i != end and lst[i] == lst[end]:
                end = len(lst)
            end += 1
        if end == len(lst):
            return lst[i]
    return None

if __name__ == "__main__":
    arr = [3, 3, 3, 4, 6, 6]
    print(find_first_unique(arr))
        

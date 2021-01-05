from stack_class import Stack

def sort_stack(s):
    temp_stack = Stack()

    while not s.isEmpty():
        value = s.pop()

        if temp_stack.top() is not None and value >= temp_stack.top():
            temp_stack.push(value)
        else:
            while not temp_stack.isEmpty():
                s.push(temp_stack.pop())
            temp_stack.push(value)

    while not temp_stack.isEmpty():
        s.push(temp_stack.pop())
    
    return s

if __name__ == "__main__":
    arr = [23, 60, 12, 42, 4, 97, 2]
    s = Stack()
    for i in arr:
        s.push(i)
    print(s.list)
    result = sort_stack(s)
    print(result.list)
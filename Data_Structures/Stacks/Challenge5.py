from stack_class import Stack
def sort_stack(stack):

    temp_stack = Stack()

    while stack.isEmpty() is False:

        value = stack.pop()

        if (temp_stack.top() is not None and 
           value >= int(temp_stack.top())):
            # if value is not none and larger, push it at the top of temp_stack
            temp_stack.push(value)
        else:
            while temp_stack.isEmpty() is False:
                stack.push(temp_stack.pop())
            # place value as the smallest element in temp_stack
            temp_stack.push(value)

    # Transfer from temp_stack => stack
    while temp_stack.isEmpty() is False:
        stack.push(temp_stack.pop())

    return stack
from stack_class import Stack

def is_balanced(exp):
    opening_paren = ['(', '{', '[']
    s = Stack()
    # If the characters are in opening_paren
    # Add them to the stack
    for char in exp:
        if char in opening_paren:
            s.push(char)
        else:
            if s.isEmpty():
                return False
            this_char = s.pop()
            if this_char == '(':
                if char != ')':
                    return False
            if this_char == '{':
                if char != '}':
                    return False
            if this_char == '[':
                if char != ']':
                    return False
    if s.isEmpty():
        return True
    else:
        return False




if __name__ == "__main__":
    exp = Stack()
    paren_string = "{[({})]}"
    paren_string2 = "{([](}"
    for p in paren_string2:
        exp.push(p)
    print(is_balanced(exp))
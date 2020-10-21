from stack_class import Stack

def sort_stack(s):
    if s.size == 0:
        return None
    interm = [s.pop() for i in range(s.size())]
    interm.sort()
    for i in range(len(interm)):
        s.push(interm.pop())
    return s

if __name__ == "__main__":
    ss = [23, 60, 12, 42, 4, 97, 2]
    s = Stack()
    for i in ss:
        s.push(i)
    s.print_stack()
    result = sort_stack(s)
    result.print_stack()

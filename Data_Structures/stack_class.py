class Stack():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, element):
        return self.items.append(element)
    
    def pop(self):
        return self.items.pop(-1)
    
    def top(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)

if __name__ == "__main__":
    s1 = Stack()
    print(s1.isEmpty())
    s1.push(45)
    s1.push(10)
    s1.push(25)
    s1.push('Alexis')
    s1.print_stack()
    print(s1.size())
    s1.pop()
    print(s1.top())
    print(s1.size())
    s1.print_stack()

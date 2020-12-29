class MinStack():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def push(self, value):
        return self.items.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def show(self):
        print(self.items)
    
    def min(self):
        temp_stack = MinStack()
        min_val = self.pop()
        self.push(min_val)
        for i in range(self.size()):
            val = self.pop()
            if val < min_val:
                min_val = val
                temp_stack.push(val)
        return min_val
                


if __name__ == "__main__":
    s = MinStack()
    arr = [23, 60, 12, 42, 4, 97, 2]
    for a in arr:
        s.push(a)
    s.show()
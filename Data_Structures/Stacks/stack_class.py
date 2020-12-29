class Stack():
    def __init__(self):
        self.list  = []
    
    def isEmpty(self):
        return self.list == []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        self.list.pop()

    def size(self):
        return len(self.list)

    def top(self):
        return self.list[-1]
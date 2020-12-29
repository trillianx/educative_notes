
class TwoStack():
    def __init__(self, size):
        self.size = size
        self.list = [0] * self.size
        
    def stackSize(self):
        return len(self.list)

    def push1(self, value):
        if self.stackSize() == self.size:
            return 'No Space'
        else:
            self.list.insert(0, value)
from stack_class import Stack

class NewQueue():
    def __init__(self):
        self.main_stack = Stack()
        self.helper_stack = Stack()

    
    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):
        n = self.main_stack.size()
        # Put all the contents of the stack
        # into the helper stack
        for i in range(n):
            self.helper_stack.push(self.main_stack.pop())
        
        # Pop the top
        self.helper_stack.pop()

        # Push all the rest back into the main stack
        for i in range(n-1):
            self.main_stack.push(self.helper_stack.pop())
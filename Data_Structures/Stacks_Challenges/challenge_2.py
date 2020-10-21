class TwoStacks:
    """
    Stack 1 is on the left while Stack 2 is on the right

                --------------------------
    stack 1 --->|    |    |    |    |    |<--stack 2
                --------------------------
    """
    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [0] * n
        # Index for stack to the left
        self.index1 = -1
        # Index for stack to the right
        self.index2 = self.size

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.index1 < self.index2 - 1:
            # Increase the index by 1
            self.index1 = self.index1 + 1
            # and then Add the element to the first stack
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to push an element x to stack2
    def push2(self, x):

        # There is at least one empty space for new element
        if self.index1 < self.index2 - 1:
            # Decrease the index by 1
            self.index2 = self.index2 - 1
            # Add the element to the second stack
            self.arr[self.index2] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()
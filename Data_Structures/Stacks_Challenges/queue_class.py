class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        return self.items[0]
    
    def back(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def show(self):
        return self.items


    @staticmethod
    def compute_binary(n):
        result = []
        queue = Queue()
        queue.enqueue(1)
        for i in range(n):
            print(i)
            result.append(str(queue.dequeue()))
            print(result)
            s1 = result[i] + "0"
            s2 = result[i] + "1"
            print(s1)
            print(s2)
            queue.enqueue(s1)
            queue.enqueue(s2)
            print(queue.items)
            print("--"* 20)
            # pdb.set_trace()
        return result


if __name__ == "__main__":
    a = Queue.compute_binary(5)
    print(a)

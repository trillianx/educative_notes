from queue_class import Queue
from stack_class import Stack

def reverseK(q, k):
    if k == 0:
        return q
    if q.size == 0:
        return None
    # check the size:
    if q.size() < k:
        return None
    
    # Define a stack: 
    s1 = Stack()
    result = []
    
    for i in range(k):
        s1.push(q.dequeue())
    for i in range(k):
        result.append(s1.pop())
    while not q.isEmpty():
        result.append(q.dequeue())
    return result


if __name__ == "__main__":
    q = Queue()
    for i in range(1,11):
        q.enqueue(i)
    print(q.show())
    print(reverseK(q, 3))
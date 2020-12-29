from queue_class import Queue
from stack_class import Stack

def reverseK(queue, k):
    if queue.is_empty() is True or k > queue.size() or k < 0:
        # Handling invalid input
        return None

    stack = Stack()
    for i in range(k):
        stack.push(queue.dequeue())

    while stack.isEmpty() is False:
        queue.enqueue(stack.pop())

    size = queue.size()

    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue

if __name__ == "__main__":
    q = Queue()
    for i in range(1, 11):
        q.enqueue(i)
    result = reverseK(q, 5)
    for i in range(q.size()):
        print(q.dequeue())
    

from queue_class import Queue

def find_bin(n):
    result = []
    q = Queue()
    q.enqueue("1")
    for i in range(n):
        result.append(q.dequeue())
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        q.enqueue(s1)
        q.enqueue(s2)
    return result

if __name__ == "__main__":
    print(find_bin(5))

    
from graph import Graph
from stack_class import Stack
from queue_class import Queue

def find_all_paths(gs, source, destination):
    # result = ""
    s = Queue()
    s.enqueue(source)
    while s.is_empty() is not True:
        result = ''
        vertex = s.dequeue()
        node = gs.array[vertex].head_node
        result += str(vertex)
        while node is not None:
            s.enqueue(node.data)
            result += str(node.data)
            node = node.next
        print(result)

if __name__ == "__main__":
    gs = Graph(4)
    gs.add_edge(0, 1)
    gs.add_edge(1, 2)
    gs.add_edge(1, 3)
    gs.add_edge(3, 2)
    # gs.add_edge(2, 4)
    # gs.add_edge(2, 5)
    # gs.add_edge(5, 0)
    gs.print_graph()
    find_all_paths(gs, 0, 2)
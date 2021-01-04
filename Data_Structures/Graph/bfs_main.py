from graph import Graph
from queue_class import Queue

def bfs(gs, source, visited):
    result = ""
    q = Queue()
    q.enqueue(source)
    while not q.is_empty():
        vertex = q.dequeue()
        this_node = gs.array[vertex].head_node
        while this_node is not None:
            if this_node.data not in visited:
                q.enqueue(this_node.data)
                visited.append(this_node.data)
                result += str(this_node.data)
            this_node = this_node.next
    return result, visited

if __name__ == "__main__":
    gs = Graph(6)
    gs.add_edge(0, 1)
    gs.add_edge(0, 2)
    gs.add_edge(1, 3)
    gs.add_edge(2, 3)
    gs.add_edge(2, 4)
    gs.add_edge(2, 5)
    gs.add_edge(5, 0)
    gs.print_graph()
    r, v = bfs(gs, 0, [])
    # print(bfs_traveral(gs, 0))
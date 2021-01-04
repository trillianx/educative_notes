from graph import Graph
from queue_class import Queue

def bfs_traversal_helper(gs, source, visited):
    result = ""
    q = Queue()
    q.enqueue(source)
    visited[source] = True
    while not q.is_empty():
        current_node = q.dequeue()
        result += str(current_node)
        temp = gs.array[current_node].head_node
        while temp is not None:
            if visited[temp.data] is False:
                q.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next
    return result, visited

def bfs_traveral(gs, source):
    result = ""
    num_of_vertices = gs.vertices
    if num_of_vertices == 0:
        return result
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    result, visited = bfs_traversal_helper(gs, source, visited)
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(gs, i, visited)
            result += result_new
    return result
    

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
    print(bfs_traveral(gs, 4))

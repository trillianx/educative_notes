from stack_class import Stack
from graph import Graph

def dfs(gs, source, visited):
    result = ""
    s = Stack()
    s.push(source)
    visited[source] = True
    while s.isEmpty() is False:
        vertex = s.pop()
        print(vertex)
        result += str(vertex)
        node = gs.array[vertex].head_node
        if node is not None:
            if node.data == source:
                print('cycle detected!')
        while node is not None:
            if visited[node.data] is False:
                s.push(node.data)
                visited[node.data] = True
            node = node.next
    return result, visited

def dfs_run(gs, source):
    result = ""
    if gs.array == []:
        return result
    num_of_vertices = len(gs.array)
    visited = [False] * num_of_vertices
    result, visited = dfs(gs, source, visited)
    for index, b in enumerate(visited):
        if b == False:
            result_new, visited = dfs(gs, index, visited)
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
    print(dfs_run(gs, 0))

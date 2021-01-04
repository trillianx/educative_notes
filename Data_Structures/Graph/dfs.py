from stack_class import Stack
from graph import Graph

def dfs_traversal_helper(gs, source, visited):
    result = ""
    s = Stack()
    s.push(source)
    visited[source] = True
    while s.isEmpty() is False:
        vertex = s.pop()
        result += str(vertex)
        node = gs.array[vertex].head_node
        while node is not None:
            if visited[node.data] is False:
                s.push(node.data)
                visited[node.data] = True
            node = node.next
    return result, visited

def dfs_traversal(gs, source):
    result = ""
    num_of_vertices = gs.vertices
    if num_of_vertices == 0:
        return result
    visited = [False] * num_of_vertices
    result, visited = dfs_traversal_helper(gs, source, visited)
    for index, tf in enumerate(visited):
        if tf == False:
            result_new, visited = dfs_traversal_helper(gs, index, visited)
            result += result_new
    return result


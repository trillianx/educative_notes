from graph import Graph
from dfs import dfs_traversal_helper

def check_path(gs, source, destination):
    visited = [False] * len(gs.array)
    result, visited = dfs_traversal_helper(gs, source, visited)
    visited_vertices = [v for v in result]
    if str(destination) in visited_vertices:
        return True
    else:
        return False


if __name__ == "__main__":
    gs = Graph(6)
    gs.add_edge(0, 1)
    gs.add_edge(0, 2)
    gs.add_edge(1, 3)
    gs.add_edge(2, 3)
    gs.add_edge(2, 4)
    gs.add_edge(2, 5)
    #gs.add_edge(5, 0)
    gs.print_graph()
    print(check_path(gs, 2, 0))

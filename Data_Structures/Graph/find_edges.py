from graph import Graph

def find_edges(gs):
    count = 0
    num_of_vertices = len(gs.array)
    for vertex in range(num_of_vertices):
        this_node = gs.array[vertex].head_node
        while this_node is not None:
            count += 1
            this_node = this_node.next
    return count

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
    print(find_edges(gs))
from linked_list_class import LinkedList

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
    
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        for v in range(self.vertices):
            print("|", v, end=" | => ")
            cur_node = self.array[v].head_node
            while cur_node != None:
                print("[", cur_node.data, end=" ] -> ")
                cur_node = cur_node.next
            print("None \n") 
        return None

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

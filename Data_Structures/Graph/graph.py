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
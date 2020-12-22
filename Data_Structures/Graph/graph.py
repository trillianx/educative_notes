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
            self.
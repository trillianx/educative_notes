[TOC]



# Graphs

## Introduction

Graph is a data structure used to store and manipulate data. Graphs are used in GPS, neural networks, peer-to-peer networks, search engine crawlers, garbage collection in python, and social network sites.  Let's look more closely to graphs. 

### Graph Structure

A **graph** is a collection of nodes that are connected to each other in the form of a network. Graph has two basics components: 

*   **Vertex** - This is the most essential part of the graph. Think of this as the node.
*   **Edge** - An edge is a link between to vertices. 

Here's how a graph is represented: 

![image-20201222131208561](Graph_notes.assets/image-20201222131208561.png)



### Graph Properties

There are several other properties that we look at now. 

*   **Degree of a Vertex** - This is defined as the total number of edges incident on a vertex. Because the edges depend on the incidents on a vertex, there are two types: 
    *   **In-degree** - these are the total number of incoming edges onto a vertex
    *   **Out-degree** - these are the total number of outgoing edges from a vertex
*   **Parallel Edges** -  Edges that do not have direction are considered parallel if they have the same two vertices. Edges that have direction are said to be parallel if they both start and end from same vertices
*   **Self Loop** - When an edge starts and ends on the same vertex, it is considered a self loop
*   **Adjacency** - Two vertices are said to be adjacent if there is an edge connecting them directly. 

To illustrate these properties, let's look at the figure above.

*   The in-degree for `a` is 1. So, is the case with `b`. `c` has in-degree of 2 and out-degree of 1. 
*   `c` contains a self loop. 

### Types of Graphs

There are two types of graphs: 

*   **Undirected Graphs** - in these graphs, the edges are bi-directional. We can see in the example below. 

    <img src="Graph_notes.assets/image-20201222133043386.png" alt="image-20201222133043386" style="zoom:80%;" />

    In the pair, (2, 3) we see that there is an edge that connects them but one can go between them in any direction. 
    The maximum number of edges in a undirected graph is given by, $n(n-1)/2$ , where $n$ is the total number of vertices.  

*   **Directed Graphs** - in these graphs, the edges have a specific direction. We can see in the example below: 

    <img src="Graph_notes.assets/image-20201222133444596.png" alt="image-20201222133444596" style="zoom:80%;" />

    Taking the same example, we see that for a pair (2, 3) there is just one way to go between 2 and 3. The total number of edges in a directed graph is $n(n-1)$, where $n$ is the total number of vertices. 

### Graph Representation

There are two common ways to represent a graph. These are: 

*   **Adjacency Matrix** - This is a 2D matrix where a cell contains a boolean. The vertex number if listed on top and the side of the matrix. Think of it as a confusion matrix but bigger. When there is an edge between the two vertices, we  represent that with `1`. The figure below shows the representation of a undirected graph in an adjacency matrix: 

    <img src="Graph_notes.assets/image-20201222134636569.png" alt="image-20201222134636569" style="zoom:80%;" />

    The adjacency matrix is different for a directed graph. When the above graph is directed, we get something like this: 

    <img src="Graph_notes.assets/image-20201222134747533.png" alt="image-20201222134747533" style="zoom:80%;" />

    We can see that the matrix is much more sparse for a directed graph than for undirected graph.
    

*   **Adjacency List** - Rather than representing with a matrix, we can represent a graph as a linked list. Each vertex has its own linked list. For a undirected graph, the adjacency list looks like this: 

    <img src="Graph_notes.assets/image-20201222135206525.png" alt="image-20201222135206525" style="zoom:80%;" />

    For a directed graph, the representation looks something like this: 
    <img src="Graph_notes.assets/image-20201222135330600.png" alt="image-20201222135330600" style="zoom:80%;" />

    

    We see that each vertex is much smaller linked list than in undirected graph. 

## Graph Implementation

Let's implement the adjacency list method of graph representation. The implementation will be for a directed graph. We will create a class and represent the following graph. 

<img src="Graph_notes.assets/image-20201222135634682.png" alt="image-20201222135634682" style="zoom:80%;" />

The graph class consists of two data members: 

*   The total number of vertices in the graph
*   A list of linked lists to store adjacent vertices

```python
from ll import LinkedList

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
```

As we have seen here, each vertex has an associated LinkedList. So, the class takes in the number of vertices. Next, we define an array which will store these vertices. Finally, we create a linked list associated with each vertex and store these linked lists into the array. So, we now have a list of linked lists. 

Next we will create few functionalities. These include: 

*   `add_edge()`
*   `print_graph()`

```python
def add_edge(self, source, destination):
    if source < self.vertices and destination < self.vertices:
        self.array[source].insert_at_head(destination)
```

This is for directed graph. If we had a undirected graph, then we would write this as: 

```python
def add_edge(self, source, destination):
    if source < self.vertices and destination < self.vertices:
        self.array[destination].insert_at_head(source)
```

Finally, here's the code to represent a graph: 

```python
def print_graph(self):
    print(">>Adjacency List of Directed Graph<<")
    print
    for i in range(self.vertices):
        print("|", i, end=" | => ")
        temp = self.array[i].get_head()
        while(temp is not None):
            print("[", temp.data, end=" ] -> ")
            temp = temp.next_element
            print("None")
```










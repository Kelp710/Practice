class Graph():
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        self.adjacency_list[data] = []
        self.number_of_nodes += 1
        return

    def insert_edge(self, vertex1, vertex2):    
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return
        return "It`s already here"

       


    
    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')

gg = Graph()
gg.insert_node(2)
gg.insert_node(1)
gg.insert_node(3)
gg.insert_edge(2,1)
gg.insert_edge(3,2)
gg.show_connections()
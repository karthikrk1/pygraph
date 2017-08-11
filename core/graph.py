"""
This class is an implementation of the Graph DS
"""
from edge import Edge

_author_name = 'karthik'

class Graph():
    vertex_list = None # This denotes a list of vertices in the graph
    is_directed = None # Initialized to None - This will denote if the graph is directed or not
    num_vertex = 0 # This is the initial number of vertices for the graph. This is initialized to 0

    def __init__(self, n):
        self.is_directed = False
        self.num_vertex = n
        self.vertex_list = [0] * n


    def get_vertex(self, n):
        return self.vertex_list[n-1]

    def add_edge(self, f, t, w):
        e = Edge(f, t, w)
        if(self.is_directed):
            f.adj.append(e)
            t.rev_adj.append(e)

        else:
            f.adj.append(e)
            t.adj.append(e)

    def size(self):
        return self.num_vertex

    






"""
This is an implementation of the vertex class
"""

_author_name = 'karthik'

class Vertex():
    name = None # Name of the vertex: Should be an int
    seen = None # boolean seen flag, this is to keep track if the vertex is seen while traversing
    adj = [] # adjacency list
    rev_adj = [] # reverse adjacency list

    def __init__(self, n):
        self.name = n
        self.seen = False # initially set to False

    def __iter__(self):
        return self.adj.__iter__()


    def __repr__(self):
        return str(self.name)

    def degree(self):
        return len(self.adj)

    # The following 2 functions can be used for directed graphs

    def outDegree(self):
        return self.degree()

    def inDegree(self):
        return len(self.rev_adj)
"""
Class to represent the edge of a graph
"""

_author_name = 'karthik'

class Edge():
    from_vertex = None
    to_vertex = None
    weight = 0

    def __init__(self, f, t, w):
        self.from_vertex = f
        self.to_vertex = t
        self.weight = w

    def otherEnd(self, u):
        if self.from_vertex == u or self.to_vertex == u:
            if self.from_vertex ==u:
                return self.to_vertex
            else:
                return self.from_vertex
        else:
            raise ValueError(str(u.name) + ' is not part of this edge')

    def __repr__(self):
        ret = '(' + self.from_vertex + ' , ' + self.to_vertex + ')'
        return ret
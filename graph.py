class Node(object):
    def __init__(self, value):
        self._value = value
        self.attr = {}

    def __str__(self):
        return "Node: " + self._value

    def __hash__(self):
        return hash((self._value, self.attr))

    def __eq__(self, other):
        # return (self.name, self.location) == (other.name, other.location)
        return (self._value, self.attr) == (other._value, other.attr)


class Graph(object):
    def __init__(self):
        self._g = {}  # Internal structure

    def add_node(self, node):
        if node not in self._g:
            self._g[node] = []

    def add_edge(self, n1, n2):
        pass

    def __getitem__(self, item):
        return self._g[item]

    def __str__(self):
        return "Graph object:\n" \
               "Number of nodes --> " + str(len(self._g)) + "\n" \
               ""
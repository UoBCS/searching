class Node(object):
    def __init__(self, value):
        self.__value = value
        self.attr = {}

    def __str__(self):
        return "Node value --> " + self.__value

    def __hash__(self):
        return hash(self.__value)

    """def __cmp__(self, other):
        return cmp(self.attr['h'], other.attr['h'])"""

    def __eq__(self, other):
        return self.__value == other.__value


class Graph(object):
    def __init__(self):
        self.__g = {}  # Internal structure

    def add_node(self, node):
        if node not in self.__g:
            self.__g[node] = []

    def add_edge(self, n1, n2):
        if n1 not in self.__g:
            self.add_node(n1)

        if n2 not in self.__g:
            self.add_node(n2)

        self.__g[n1].append(n2)
        self.__g[n2].append(n1)

    def __getitem__(self, item):
        return self.__g[item]

    def __str__(self):
        return str(self.__g)

def bfs(G, s, f):
    """
    Breadth-first search
    :param G: The graph object
    :param s: The start node
    :param f: The goal node
    :return: The explored set
    """
    explored, frontier = [], [s]

    while frontier:
        v = frontier.pop(0)
        if v == f:
            pass
        else:
            explored.append(v)
            frontier.extend([w for w in G[v] if w not in explored])

    return explored


def dfs(G, s, f):
    """
    Depth-first search
    :param G: The graph object
    :param s: The start node
    :param f: The goal node
    :return: The explored set
    """
    explored, frontier = [], [s]

    while frontier:
        v = frontier.pop()
        if v == f:
            pass
        else:
            explored.append(v)
            frontier.extend([w for w in G[v] if w not in explored])

    return explored
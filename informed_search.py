import inspect
import priority_queue as pq


def greedy_best_first_search(G, h, s, f):
    """

    :param G:
    :param h:
    :param s:
    :param f:
    :return:
    """
    if not inspect.isfunction(h):
        return False

    explored, frontier = [], pq.PriorityQueue('h')
    frontier.enqueue(s)

    while frontier:
        v = frontier.dequeue()
        if v == f:
            pass
        else:
            if v not in explored:
                explored.append(v)

                for w in G[v]:
                    pass

                frontier.extend([w for w in G[v] if w not in explored])

    return explored


def a_star_search(G, h, s, f):
    pass


def simulated_annealing(G, h, s, f):
    pass
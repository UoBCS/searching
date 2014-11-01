import Queue

def greedy_best_first_search(G, s, f):
    """

    :param G:
    :param h:
    :param s:
    :param f:
    :return:
    """

    explored, frontier = [], Queue.PriorityQueue()
    frontier.put(s)

    while not frontier.empty():
        v = frontier.get()
        if v == f:
            pass
        else:
            if v not in explored:
                explored.append(v)

                for w in G[v]:
                    if w not in explored:
                        frontier.put(w)

    return explored

"""q = Queue.PriorityQueue()

q.put( Job(3, 'Mid-level job') )
q.put( Job(10, 'Low-level job') )
q.put( Job(1, 'Important job') )

while not q.empty():
    next_job = q.get()
    print 'Processing job:', next_job.description"""


def a_star_search(G, s, f):
    pass


def simulated_annealing(G, s, f):
    pass
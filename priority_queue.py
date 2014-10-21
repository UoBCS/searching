class PriorityQueue(object):
    def __init__(self, func):
        self.func = func
        self.queue = []

    def enqueue(self, node):
        self.queue.append(node)
        sorted(self.queue, key=lambda x: x.attr['h'])

    def dequeue(self):
        return self.queue.pop(0)
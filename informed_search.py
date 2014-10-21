import inspect

class PriorityQueue(object):
	def __init__(self, func):
		self.func = func
		self.queue = []
	
	def enqueue(self, val):
		pass
		
	def dequeue(self):
		return self.queue.pop(0)

def greedy_best_first_search(G, h, s, f):
	"""
	G = {
		'a': ['b', 'c'],
		'b': ['a', 'c'],
		'c': ['a']
	}
	"""
	if not inspect.isfunction(h):
		return False
	
	explored, frontier = [], [s]
	
	while frontier:
		v = frontier.pop(0)
		if v == f:
			pass
		else:
			if v not in explored:
				explored.append(v)
				
				for w in G[v]:
					
					pass
					
				frontier.extend([w for w in G[v] if w not in explored])
	
	return explored

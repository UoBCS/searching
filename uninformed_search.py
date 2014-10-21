
def bfs(G, s, f):
	"""
	G = {
		'a': ['b', 'c'],
		'b': ['a', 'c'],
		'c': ['a']
	}
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
	"""
	explored, frontier = [], [s]
	
	while frontier:
		v = frontier.pop()
		if v == f:
			pass
		else:
			explored.append(v)
			frontier.extend([w for w in G[v] if not in explored])
		
	return explored

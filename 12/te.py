from collections import deque, defaultdict

def read2(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def n_paths(G, src, dst):
	stack = deque([(src, {src})])
	total = 0

	while stack:
		node, visited = stack.pop()
		if node == dst:
			total += 1
			continue

		for n in G[node]:
			if n in visited and n.islower():
				continue

			stack.append((n, visited | {n}))

	return total

def n_paths2(G, src, dst):
	stack = deque([(src, {src}, False)])
	total = 0

	while stack:
		node, visited, double = stack.pop()
		if node == dst:
			total += 1
			continue

		for n in G[node]:
			if n not in visited or n.isupper():
				stack.append((n, visited | {n}, double))
				continue

			if double:
				continue

			stack.append((n, visited, True))

	return total

G = defaultdict(list)
for edge in read2('sample2'):
	a, b = edge.rstrip().split('-')

	if b != 'start':
		G[a].append(b)
	if a != 'start':
		G[b].append(a)
print(G)
print(n_paths(G, 'start', 'end'))
print(n_paths2(G, 'start', 'end'))
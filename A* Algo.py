A* ALGORITHM:
# graph class
class Graph:

# init class
def __init__(self, graph_dict=None, directed=True):
self.graph_dict = graph_dict or {}
self.directed = directed
if not directed:
self.make_undirected()

# create undirected graph by adding symmetric edges
def make_undirected(self):
for a in list(self.graph_dict.keys()):
for (b, dist) in self.graph_dict[a].items():
self.graph_dict.setdefault(b, {})[a] = dist

# add link from A and B of given distance, and also add the inverse link if the graph is
undirected
def connect(self, A, B, distance=1):
self.graph_dict.setdefault(A, {})[B] = distance
if not self.directed:
self.graph_dict.setdefault(B, {})[A] = distance

2

# get neighbors or a neighbor
def get(self, a, b=None):
links = self.graph_dict.setdefault(a, {})
if b is None:
return links
else:
return links.get(b)

# return list of nodes in the graph
def nodes(self):
s1 = set([k for k in self.graph_dict.keys()])
s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
nodes = s1.union(s2)
return list(nodes)

# node class
class Node:
# init class
def __init__(self, name:str, parent:str):
self.name = name
self.parent = parent
self.g = 0 # distance to start node
self.h = 0 # distance to goal node
self.f = 0 # total cost

# compare nodes
def __eq__(self, other):
return self.name == other.name

# sort nodes
def __lt__(self, other):
return self.f &lt; other.f

2

# print node
def __repr__(self):
return (&#39;({0},{1})&#39;.format(self.name, self.f))

# A* search
def astar_search(graph, heuristics, start, end):

# lists for open nodes and closed nodes
open = []
closed = []

# a start node and an goal node
start_node = Node(start, None)
goal_node = Node(end, None)

# add start node
open.append(start_node)

# loop until the open list is empty
while len(open) &gt; 0:

open.sort() # sort open list to get the node with the lowest cost first
current_node = open.pop(0) # get node with the lowest cost
closed.append(current_node) # add current node to the closed list

# check if we have reached the goal, return the path
if current_node == goal_node:
path = []
while current_node != start_node:
path.append(current_node.name + &#39;: &#39; + str(current_node.g))
current_node = current_node.parent

2

path.append(start_node.name + &#39;: &#39; + str(start_node.g))
return path[::-1]

neighbors = graph.get(current_node.name) # get neighbours

# loop neighbors
for key, value in neighbors.items():
neighbor = Node(key, current_node) # create neighbor node
if(neighbor in closed): # check if the neighbor is in the closed list
continue

# calculate full path cost
neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
neighbor.h = heuristics.get(neighbor.name)
neighbor.f = neighbor.g + neighbor.h

# check if neighbor is in open list and if it has a lower f value
if(add_to_open(open, neighbor) == True):

# everything is green, add neighbor to open list
open.append(neighbor)

# return None, no path is found
return None

# check if a neighbor should be added to open list
def add_to_open(open, neighbor):
for node in open:
if (neighbor == node and neighbor.f &gt; node.f):
return False
return True

2

# create a graph
graph = Graph() # user-based input for edges will be updated in the upcoming days
# create graph connections (Actual distance)
graph.connect(&#39;Frankfurt&#39;, &#39;Wurzburg&#39;, 111)
graph.connect(&#39;Frankfurt&#39;, &#39;Mannheim&#39;, 85)
graph.connect(&#39;Wurzburg&#39;, &#39;Nurnberg&#39;, 104)
graph.connect(&#39;Wurzburg&#39;, &#39;Stuttgart&#39;, 140)
graph.connect(&#39;Wurzburg&#39;, &#39;Ulm&#39;, 183)
graph.connect(&#39;Mannheim&#39;, &#39;Nurnberg&#39;, 230)
graph.connect(&#39;Mannheim&#39;, &#39;Karlsruhe&#39;, 67)
graph.connect(&#39;Karlsruhe&#39;, &#39;Basel&#39;, 191)
graph.connect(&#39;Karlsruhe&#39;, &#39;Stuttgart&#39;, 64)
graph.connect(&#39;Nurnberg&#39;, &#39;Ulm&#39;, 171)
graph.connect(&#39;Nurnberg&#39;, &#39;Munchen&#39;, 170)
graph.connect(&#39;Nurnberg&#39;, &#39;Passau&#39;, 220)
graph.connect(&#39;Stuttgart&#39;, &#39;Ulm&#39;, 107)
graph.connect(&#39;Basel&#39;, &#39;Bern&#39;, 91)
graph.connect(&#39;Basel&#39;, &#39;Zurich&#39;, 85)
graph.connect(&#39;Bern&#39;, &#39;Zurich&#39;, 120)
graph.connect(&#39;Zurich&#39;, &#39;Memmingen&#39;, 184)
graph.connect(&#39;Memmingen&#39;, &#39;Ulm&#39;, 55)
graph.connect(&#39;Memmingen&#39;, &#39;Munchen&#39;, 115)
graph.connect(&#39;Munchen&#39;, &#39;Ulm&#39;, 123)
graph.connect(&#39;Munchen&#39;, &#39;Passau&#39;, 189)
graph.connect(&#39;Munchen&#39;, &#39;Rosenheim&#39;, 59)
graph.connect(&#39;Rosenheim&#39;, &#39;Salzburg&#39;, 81)
graph.connect(&#39;Passau&#39;, &#39;Linz&#39;, 102)
graph.connect(&#39;Salzburg&#39;, &#39;Linz&#39;, 126)
# make graph undirected, create symmetric connections
graph.make_undirected()
# create heuristics (straight-line distance, air-travel distance)
heuristics = {}

2

heuristics[&#39;Basel&#39;] = 204
heuristics[&#39;Bern&#39;] = 247
heuristics[&#39;Frankfurt&#39;] = 215
heuristics[&#39;Karlsruhe&#39;] = 137
heuristics[&#39;Linz&#39;] = 318
heuristics[&#39;Mannheim&#39;] = 164
heuristics[&#39;Munchen&#39;] = 120
heuristics[&#39;Memmingen&#39;] = 47
heuristics[&#39;Nurnberg&#39;] = 132
heuristics[&#39;Passau&#39;] = 257
heuristics[&#39;Rosenheim&#39;] = 168
heuristics[&#39;Stuttgart&#39;] = 75
heuristics[&#39;Salzburg&#39;] = 236
heuristics[&#39;Wurzburg&#39;] = 153
heuristics[&#39;Zurich&#39;] = 157
heuristics[&#39;Ulm&#39;] = 0
# run the search algorithm
path = astar_search(graph, heuristics, &#39;Frankfurt&#39;, &#39;Ulm&#39;)
print(&quot;Path:&quot;, path)

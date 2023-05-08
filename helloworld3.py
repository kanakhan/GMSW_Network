import networkx as nx
import matplotlib.pyplot as plt

D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),
                  (4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels = True)

G = nx.Graph()
G.add_nodes_from(['a','b','c','d'])
G.add_edges_from([('a','b'),('a','c'),
                  ('b','c'), ('c','d')])
nx.draw(G, with_labels = True, node_color = 'blue')

plt.show()
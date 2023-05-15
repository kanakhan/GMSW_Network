import networkx as nx
import matplotlib.pyplot as plt
#컴포넌트와 클러스터링은 따로 분석해야함


G = nx.read_weighted_edgelist('edge_list.txt',
                              delimiter = " ")
population = {

    'Kolkata' : 4486679,
    'Delhi' : 11007835,
    'Mumbai' : 12442373,
    'Guwahati' : 957352,
    'Bangalore' : 8436675,
    'Pune' : 3124458,
    'Hyderabad' : 6809970,
    'Chennai' : 4681087,
    'Thiruvananthapuram' : 460468,
    'Bhubaneshwar' : 837737,
    'Varanasi' : 1198491,
    'Surat' : 4467797,
    'Goa' : 40017,
    'Chandigarh' : 961587,
}

for i in list(G.nodes()):
    G.nodes[i]['population'] = population[i]

node_color = [G.degree(v) for v in G]
node_size = [0.0005 * nx.get_node_attributes(G,'population')[v] for v in G]
edge_width = [0.0015 * G[u][v]['weight'] for u, v in G.edges()]


plt.axis('off')
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx(G, pos, node_size = node_size,
                 node_color = node_color, alpha = 0.7,
                 with_labels = True, width = edge_width,
                 edge_color = '.4', cmap = plt.cm.Blues)

print(nx.degree_centrality(G))
plt.show()
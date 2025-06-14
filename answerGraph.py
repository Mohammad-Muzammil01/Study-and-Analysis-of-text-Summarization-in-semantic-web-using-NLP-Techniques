import networkx as nx
import matplotlib.pyplot as plt

relationships = [('trees', 'whispered', 'secrets'), ('rivers', 'sang', 'songs'), ('monkey', 'swung', 'vine'), ('monkey', 'swung', 'vine'), ('he', 'noticed', 'parrot'), ('he', 'perched', 'tree'), ('he', 'watching', 'him'), ('I', 'looking', 'something'), ('Azul', 'fluffed', 'feathers'), ('you', 'visit', 'Falls'), ('jungle', 'shares', 'secrets'), ('jungle', 'shares', 'those'), ('Tiko', 'followed', 'directions'), ('Tiko', 'navigating', 'vines'), ('Tiko', 'glowing', 'mushrooms'), ('he', 'heard', 'roar'), ('he', 'reached', 'falls'), ('he', 'saw', 'something'), ('he', 'reflecting', 'jungle'), ('Tiko', 'saw', 'reflection'), ('Tiko', 'saw', 'animals'), ('jaguar', 'was', 'him'), ('jungle', 'showing', 'him'), ('jungle', 'showing', 'world'), ('it', 'revealing', 'what'), ('he', 'returned', 'troop'), ('he', 'searched', 'something'), ('he', 'shared', 'wisdom'), ('he', 'teaching', 'others'), ('he', 'appreciate', 'mysteries'), ('he', 'hidden', 'sight'), ('jungle', 'whispered', 'secret'), ('discoveries', 'come', 'those'), ('who', 'seek', 'eyes')]

G = nx.DiGraph()

for subject, relation, obj in relationships:
    G.add_edge(subject, obj, label=relation)

pos = nx.spring_layout(G, seed=42, k=0.8)

plt.figure(figsize=(15, 15))
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='red')

plt.axis('off')
plt.show()

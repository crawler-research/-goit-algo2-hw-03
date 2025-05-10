import networkx as nx

G = nx.DiGraph()

G.add_edge('source', 'T1', capacity=100)
G.add_edge('source', 'T2', capacity=100)

edges_term_to_ware = [
    ('T1','W1',25), ('T1','W2',20), ('T1','W3',15),
    ('T2','W3',15), ('T2','W4',30), ('T2','W2',10)
]
G.add_edges_from([(u, v, {'capacity': c}) for u, v, c in edges_term_to_ware])

edges_ware_to_store = [
    ('W1','S1',15), ('W1','S2',10), ('W1','S3',20),
    ('W2','S4',15), ('W2','S5',10), ('W2','S6',25),
    ('W3','S7',20), ('W3','S8',15), ('W3','S9',10),
    ('W4','S10',20),('W4','S11',10),('W4','S12',15),
    ('W4','S13',5), ('W4','S14',10)
]
G.add_edges_from([(u, v, {'capacity': c}) for u, v, c in edges_ware_to_store])

for s in [f'S{i}' for i in range(1, 15)]:
    G.add_edge(s, 'sink', capacity=100)

flow_value, flow_dict = nx.maximum_flow(G, 'source', 'sink')
print('Максимальний потік мережі:', flow_value)

print(flow_dict)
import networkx as nx

def parse_neo4j_to_nx(results):
    #id_pattern = re.compile(r".+/(\d+)$")
    G = nx.DiGraph()
    
    neo4j2node = {}
    
    # first pass add nodes
    num_nodes = 0
    for r in results:
#         print r[0]
#         node_id = id_pattern.search(r[1]['start']).group(1)
        node_id = r[0].id
        if node_id not in G:
#             print 'adding',node_id
            neo4j2node[node_id] = num_nodes
            G.add_node(node_id, 
#                        neo4j_id=node_id,
#                        city=r[0]['city'],
#                                 firstName=r[0]['firstName'],
#                                 lastName=r[0]['lastName'],
                                taxonomyCode=r[0].properties['taxonomyCode'])
            num_nodes += 1

    
    # now add edges
    num_edges = 0
    for r in results:
#         node_id = id_pattern.search(r[1]['start']).group(1)
#         to_id = id_pattern.search(r[1]['end']).group(1)
#         edge_id = id_pattern.search(r[1]['self']).group(1)
        node_id = r[0].id
        to_id = r[2].id
        edge_id = r[1].id
        
#         start = neo4j2node[node_id]
#         if to_id in neo4j2node:
#             end = neo4j2node[to_id]
#         print node_id, node_id in G, to_id, to_id in G
#         if (start in G and end in G):
        if (node_id in G and to_id in G):
    #             print 'adding edge',node_id,to_id
                num_edges += 1
                G.add_edge(node_id, to_id, edge_id=edge_id)
#                 G.add_edge(start, end, edge_id=edge_id)
        
    print 'nodes:', num_nodes, 'edges:', num_edges
    return G
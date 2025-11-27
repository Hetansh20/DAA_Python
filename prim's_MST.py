#define graph
a,b,c,d,e,f = 0, 1, 2, 3, 4, 5
garph = [[a,b,2], [a,c,2], [a,d,2], [b,d,1], [b,e,5], [c,d,3], [d,e,2], [e,f,5]]

#define the adjacency matrix
def adj_matrix(V, G):
    adj = [[0 for i in range(V)] for j in range(V)]
    for i in range(len(G)):
        adj[G[i][0]][G[i][1]] = G[i][2]
        adj[G[i][1]][G[i][0]] = G[i][2]
    return adj

def prims(V, G):
    adj = adj_matrix(V, G)
    src_vertex = 0 #Source Vertex
    edges = []
    visited = []
    min_edge = [None, None, float('inf')]
    
    MST = []
    while(len(MST) != V - 1):
        visited.append(src_vertex)
        for ed in range(0,V):
            if(adj[src_vertex][ed] != 0):
                edges.append([src_vertex, ed, adj[src_vertex][ed]])
            
        for ed in range(len(edges)):
            if(edges[ed][2] < min_edge[2] and edges[ed][1] not in visited):
                min_edge = edges[ed]
                
        MST.append(min_edge)
        src_vertex = min_edge[1]
        min_edge = [None, None, float('inf')]
        
    return MST
    
print(prims(6, garph))
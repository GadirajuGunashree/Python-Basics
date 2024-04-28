# adjacency matrix construction

 n = no.of nodes 
 m = no.of edges
 n, m = map(int, input().split())
# # construct matrix of size n * n 
# # n = 4
 adj = []
 for i in range(n): # i = 0, 1, 2, 3
     row = []
     for j in range(n):
         row.append(0)
     adj.append(row)
 # adj = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
 
 for i in range(m):
     # 2 5
     u, v = map(int, input().split())
     adj[u][v] = 1 
     adj[v][u] = 1
 print(adj)

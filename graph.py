#problem1 prim's algorithm
# import heapq
#
# def prim(n,edges):
#     graph=[[]for _ in range(n)]
#     for u,v,w in edges:
#         graph[u].append((w,v))
#         graph[v].append((w,u))
#     visited=[False]*n
#     min_heap=[(0,0,-1)]
#     total=0
#     mst_edges=[]
#     while min_heap:
#         cost,u,parent=heapq.heappop(min_heap)
#         if visited[u]:
#             continue
#         visited[u]=True
#         total+=cost
#         if parent!=-1:
#             mst_edges.append((parent,u,cost))
#         for w,v in graph[u]:
#             if not visited[v]:
#                 heapq.heappush(min_heap,(w,v,u))
#
#     return total, mst_edges
#
#
# edges = [
# (0, 2, 45),
# (0, 3, 10),
# (0, 4, 40),
# (1, 2, 25),
# (1, 4, 15),
# (1, 5, 35),
# (2, 0, 45),
# (2, 1, 25),
# (2, 4, 30),
# (2, 7, 50),
# (3, 0, 10),
# (3, 7, 20),
# (4, 0, 40),
# (4, 1, 15),
# (4, 2, 30),
# (5, 1, 35),
# (5, 6, 55),
# (5, 7, 60),
# (6, 5, 55),
# (7, 2, 50),
# (7, 3, 20),
# (7, 5, 60)
# ]
# n = 8
# total, mst_edges = prim(n, edges)
# print("Prim's MST cost:", total)
# print("Prim's MST edges:", mst_edges)
#problem2 kruskal's algorithm
# def find(parent,x):
#     if parent[x] !=x:
#         parent[x]=find(parent,parent[x])
#     return parent[x]
# def union(parent,a,b):
#     ra=find(parent,a)
#     rb=find(parent,b)
#     if ra!=rb:
#         parent[rb]=ra
# def kruskal(edges,n):
#     edges.sort(key=lambda x:x[2])
#     parent=[i for i in range(n)]
#     total_cost=0
#     mst_edges=[]
#     for u,v,cost in edges:
#         if find(parent,u)!=find(parent,v):
#             union(parent,u,v)
#             total_cost+=cost
#             mst_edges.append((u,v,cost))
#     return total_cost,mst_edges
#
# edges = [
# (0, 2, 45),
# (0, 3, 10),
# (0, 4, 40),
# (1, 2, 25),
# (1, 4, 15),
# (1, 5, 35),
# (2, 0, 45),
# (2, 1, 25),
# (2, 4, 30),
# (2, 7, 50),
# (3, 0, 10),
# (3, 7, 20),
# (4, 0, 40),
# (4, 1, 15),
# (4, 2, 30),
# (5, 1, 35),
# (5, 6, 55),
# (5, 7, 60),
# (6, 5, 55),
# (7, 2, 50),
# (7,
#  3, 20),
# (7, 5, 60)]
# n = 8
# total, mst_edges = kruskal(edges, n)
# print("Kruskal MST cost:", total)
# print("Kruskal MST edges:", mst_edges)
#problem3 dijkstra's algorithm
# def dijkstra(u,n,G):
#     S=[False for x in range(n)]
#     dist=[x for x in G(u)]
#     S[u]=True
#     for _ in range(n-1):
#         min_dist=float('inf')
#         v=-1
#         for j in range(n):
#             if not S[j] and dist[j]<min_dist:
#                 min_dist=dist[j]
#                 v=j
#         if v==-1:
#             break
#         S[v]=True
#         for w in range(n):
#             if not S[w]:
#                 dist[w]=min(dist[w],dist[v]+G[v][w])
#     return dist
#
# INF =float('inf')
# n =4
# G=[
# [0, 30, 25, 40],
# [INF, 0, 10, INF],
# [20, INF, 0, 5],
# [10, INF, 15, 0]
# ]
# start = 0
# result = dijkstra(start, n, G)
# print (result)
#problem4 floyed-warshall's algorithm
def floyd(G):
    n=len(G)
    A=[[x for x in y] for y in G]
    for k in range(n):
        for v in range(n):
            for w in range(n):
                A[v][w]=min(A[v][w],A[v][k]+A[k][w])
    return A

edges =[
(0, 1, 30),
(0, 2, 25),
(0, 3, 40),
(1, 2, -10),
(2, 0, 20),
(2, 3, 5),
(3, 0, 10),
(3,2,15)
]

INF = float('inf')
n = 4
G = [[INF]*n for _ in range (n) ]
for i in range (n):
    G[i][i] = 0
for u, v, w in edges:
    G[u] [v] = w

result = floyd (G)
for row in result:
    print(row)
from collections import deque

def bfs(G,s,N):
    dist=[-1]*N
    d=deque()
    dist[s]=0
    d.append(s)
    while(len(d)!=0):
        v=d[0]
        d.popleft()
        for nv in G[v]:
            if(dist[nv]!=-1):
                continue
            dist[nv]=dist[v]+1
            d.append(nv)
            
    return dist
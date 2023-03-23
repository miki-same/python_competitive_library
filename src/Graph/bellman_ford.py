def bellman_ford(s,N,Edge,INF=10**18):
    dist=[INF]*N
    dist[s]=0
    cnt=0
    neg=False
    while True:
        update=False
        for f,t,c in Edge:
            if dist[t]>dist[f]+c:
                if cnt<N-1:
                    if dist[f]!=INF:
                        dist[t]=min(dist[t],dist[f]+c)
                        update=True
                else:
                    neg=True
        if not update:
            break
        cnt+=1
    if neg:
        return -1
    else:
        return dist
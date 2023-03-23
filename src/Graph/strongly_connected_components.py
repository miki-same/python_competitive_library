def SCC(G,n):
    rG=[[] for _ in range(n)]
    for v in range(n):
        for nv in G[v]:
            rG[nv].append(v)
        
    seen=[0]*n
    order=[]
    for v in range(n):
        if seen[v]:
            continue
        stack=[~v,v]
        while stack:
            v=stack.pop()
            if v>=0:
                if seen[v]:
                    continue
                seen[v]=1
                for nv in G[v]:
                    if not seen[nv]:
                        stack.append(~nv)
                        stack.append(nv)
            else:
                if seen[~v]==2:
                    continue
                seen[~v]=2
                order.append(~v)
        
    C=0
    group=[-1]*n
    for v in order[::-1]:
        if group[v]!=-1:
            continue
        stack=[v]
        while stack:
            v=stack.pop()
            group[v]=C
            for nv in rG[v]:
                if group[nv]==-1:
                    stack.append(nv)
        C+=1
    
    return group
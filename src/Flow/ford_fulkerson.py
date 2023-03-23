class FlowNode:
    def __init__(self,to,cap,ind):
        self.to,self.cap,self.ind=to,cap,ind
    def items(self):
        return self.to,self.cap,self.ind

class FordFulkerson:
    def __init__(self,N):
        self.G=[[] for _ in range(N)]
        self.N=N
        self.edges=[]

    def add_edge(self,u,v,cap):
        self.edges.append((u,v,cap))
        self.G[u].append(FlowNode(v,cap,len(self.G[v])))
        self.G[v].append(FlowNode(u,0,len(self.G[u])-1))
        return len(self.edges)-1

    def dfs(self,G,v,t,f,used):
        if v==t:
            return f
        used[v]=True
        for i in range(len(G[v])):
            nv,cap,ind=G[v][i].items()
            if not used[nv] and cap>0:
                d=self.dfs(self.G,nv,t,min(f,cap),used)
                if d>0:
                    self.G[v][i].cap-=d
                    self.G[nv][ind].cap+=d
                    return d
        return 0

    def Max_Flow(self,s,t):
        flow=0
        while(True):
            used=[False]*self.N
            f=self.dfs(self.G,s,t,float('inf'),used)
            if f==0:
                return flow
            flow+=f
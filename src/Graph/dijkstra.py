from heapq import heappush,heappop,heapify

class Dijkstra:
    def __init__(self,G,n,s,set_INF=float('inf')):
        self.INF=set_INF
        self.G=G
        self.n=n
        self.s=s
        self.dist=[self.INF for i in range(self.n)]
        self.prev=[-1 for i in range(self.n)]
        self.path=[[] for i in range(self.n)]
        self.done=False
        
    def get_all_dist(self):
        if self.done:
            return self.dist

        que=[(0,self.s)]
        self.dist=[self.INF]*self.n
        self.dist[self.s]=0
        while que:
            mincost,u=heappop(que)
            if(mincost>self.dist[u]):
                continue
            for c,v in self.G[u]:
                if(self.dist[u]+c<self.dist[v]):
                    self.dist[v]=self.dist[u]+c
                    self.prev[v]=u
                    heappush(que,(self.dist[v],v))
        
        self.done=True
        
        return self.dist
    
    def get_shortest_path(self, t):
        if not self.done:
            return False
        if self.dist[t]==self.INF:
            return -1
        if len(self.path[t])!=0:
            return self.path[t]
        u=t
        while u!=-1:
            self.path[t].append(u)
            u=self.prev[u]
        self.path[t]=self.path[t][::-1]
        
        return self.path[t]
    
    def is_done(self):
        return self.done
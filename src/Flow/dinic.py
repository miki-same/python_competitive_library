class MFGraph:

    def __init__(self, N,INF=10**15):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.iter=[0]*N
        self.level=[-1]*N

        self.INF=INF

    def add_edge(self, frm, to, cap):
        e = [to, len(self.G[to]), cap]
        self.G[frm].append(e)

        re=[frm, len(self.G[frm])-1, 0]
        self.G[to].append(re)
    
    def _bfs(self,s):
        self.level=[-1]*self.N
        self.level[s]=0
        que=[s]
        que_left=0

        while que_left<len(que):
            v=que[que_left]
            que_left+=1
            for to,_,cap in self.G[v]:
                if cap==0 or self.level[to]!=-1:
                    continue
                self.level[to]=self.level[v]+1
                que.append(to)
    
    def _dfs(self,s,t):
        stack=[(~s,-1),(s,-1)]
        reached=False
        nodes=[]

        while stack:
            v,l=stack.pop()

            if v>=0:
                nodes.append((v,l))
                if v==t:
                    reached=True
                    break

                for i in range(self.iter[v],len(self.G[v])):
                    self.iter[v]=i
                    to,rev,cap=self.G[v][i]
                    if cap>0 and self.level[v]<self.level[to]:
                        stack.append((~to,i))
                        stack.append((to,i))
            
            else:
                v=~v
                nodes.pop()
        
        if not reached:
            return 0
        
        f=self.INF
        for i in range(len(nodes)-1):
            v,l=nodes[i]
            nv,j=nodes[i+1]
            f=min(f,self.G[v][j][2])
        
        if f==0:
            return f

        for i in range(len(nodes)-1):
            v,l=nodes[i]
            nv,j=nodes[i+1]
            self.G[v][j][2]-=f
            self.G[nv][self.G[v][j][1]][2]+=f
        
        return f

    def max_flow(self, s, t):
        flow=0

        while True:
            self._bfs(s)
            if self.level[t]<0:
                return flow
            self.iter=[0]*self.N
            f=self._dfs(s,t)
            while f>0:
                flow+=f
                f=self._dfs(s,t)
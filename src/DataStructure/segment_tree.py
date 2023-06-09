'''
抽象化非再帰セグメント木

SegmentTree(n,op,e):
長さnの配列Sを作成
eを単位元とする演算opによる区間取得が可能

update(i,x):
S[i]をxで更新 O(logN)

get(i):
S[i]を取得 O(1)

query(l,r):
op(S[l],S[l+1],....S[r-1])を計算 O(logN)
'''

class SegmentTree:
    def __init__(self,n,op,e):
        self.e=e
        self.op=op
        self.size=1<<(n-1).bit_length()
        self.SEG=[self.e]*(self.size*2)
    
    def update(self,i,x):
        i+=self.size
        self.SEG[i]=x
        
        while i>0:
            i>>=1
            self.SEG[i]=self.op(self.SEG[i*2],self.SEG[i*2+1])
    
    def get(self,i):
        return self.SEG[i+self.size]
    
    def query(self,l,r):
        l+=self.size
        r+=self.size
        
        lres,rres=self.e,self.e
        
        while l<r:
            if l&1:
                lres=self.op(lres,self.SEG[l])
                l+=1
            
            if r&1:
                r-=1
                rres=self.op(self.SEG[r],rres)
            
            l>>=1
            r>>=1
            
        res=self.op(lres,rres)
        return res
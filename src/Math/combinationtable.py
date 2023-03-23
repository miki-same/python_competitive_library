MOD=10**9+7

class CombinationTable:
    """
    N以下の値に関する組み合わせの数・順列の数を高速に計算する。
    
    Attributes
    ----------
    N: int
    MOD: int
    """

    def __init__(self,N,MOD=10**9+7):
        self.N=N
        self.MOD=MOD

        self.fac=[0]*(N+1)
        self.fac[0]=1
        self.fac[1]=1
        self.finv=[0]*(N+1)
        self.finv[0]=1
        self.finv[1]=1
        self.inv=[0]*(N+1)
        self.inv[1]=1

        for i in range(2,N+1):
            self.fac[i]=self.fac[i-1]*i%MOD
            self.finv[i]=self.finv[i-1]*self.inv[i]%MOD
            self.inv[i]=MOD-self.inv[MOD%i]*(MOD//i)%MOD
    
    def Combination(self,n,r):
        """
        nCrをMODで割った余りを計算する。

        Parameters
        ----------
        n: int
        r: int

        Returns
        -------
        x: int
            nCrをMODで割った余り
        """

        if n<r or r<0:
            return 0
        else:
            return ((self.fac[n]*self.finv[r])%MOD*self.finv[n-r])%MOD

    def Permutation(self,n,r):
        """
        nCrをMODで割った余りを計算する。

        Parameters
        ----------
        n: int
        r: int

        Returns
        -------
        x: int
            nCrをMODで割った余り
        """
        
        if n<r or r<0:
            return 0
        else:
            return (self.fac[n]*self.finv[n-r]%MOD)
        

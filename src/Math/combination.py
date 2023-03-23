def comb(n,k,MOD=10**9+7):
    """
    nCkをMODで割った余りを計算する。

    Parameters
    ----------
    n: int
    k: int
    
    Returns
    -------
    x: int
        nCrをMODで割った余り
    """
    
    res=1
    tmp=1
    for i in range(1,k+1):
        res=res*(n-i+1)%MOD
        tmp=tmp*i%MOD
    a=pow(tmp,MOD-2,MOD)
    return res*a%MOD
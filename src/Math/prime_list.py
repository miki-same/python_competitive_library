def primes(N):
    """
    0以上N以下の素数を全て求める。
    
    Parameters
    ----------
    N: int
        
    Returns
    -------
    p: list
        0以上N以下の素数の配列
    """

    if N==1 or N==0:
        return []
    arr=[True]*(N+1)
    arr[0],arr[1]=False,False
    p=[]
    for i in range(2,N+1):
        if arr[i]==False:
            continue
        p.append(i)
        for j in range(i*2,N+1,i):
            arr[j]=False
    return p
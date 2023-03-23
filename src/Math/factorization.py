def factorization(N):
    """
    整数を素因数分解する。
    
    Parameters
    ----------
    N: int
        素因数分解する整数
        
    Returns
    -------
    arr: list
        Nの素因数の配列
    """

    arr=[]
    tmp=N
    for i in range(2,int(N**0.5)+1):
        if(tmp%i==0):
            cnt=0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            arr.append([i,cnt])
    if(tmp!=1):
        arr.append([tmp,1])
    
    return arr
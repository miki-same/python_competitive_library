def factor(N):
    """
    整数の約数を全て求める。
    
    Parameters
    ----------
    N: int
        約数を求める整数
        
    Returns
    -------
    arr: list
        Nの素因数の配列
    """


    arr=[]
    for i in range(1,int(N**0.5)+1):
        if(N%i==0):
            arr.append(i)
            if(N//i!=i):
                arr.append(N//i)
    return arr
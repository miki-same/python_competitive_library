def is_prime(N):
    """
    整数が素数か判定する。
    
    Parameters
    ----------
    N: int
        素数判定を行う整数
        
    Returns
    -------
    flag: bool
        Nが素数のときTrue, 素数でないときFalse
    """

    for i in range(2,int(N**0.5)+1):
        if(N%i)==0:
            return False
    return True
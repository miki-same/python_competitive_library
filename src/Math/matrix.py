def mul(A,B):
    """
    行列A、行列Bの積を求める
    
    Parameters
    ----------
    A: list[list]
    B: list[list]
        
    Returns
    -------
    C: list[list]
        A@B
    """

    C=[[0]*len(B) for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j]=(C[i][j]+A[i][k]*B[k][j])
    return C

def matpow(A,N):
    """
    正方行列AのN乗を求める
    
    Parameters
    ----------
    A: list[list]
        
    Returns
    -------
    B: list[list]
        A^N
    """

    B=[[0]*len(A) for i in range(len(A))]
    for i in range(len(A)):
        B[i][i]=1
    while(N>0):
        if N&1:
            B=mul(B,A)
        A=mul(A,A)
        N>>=1
    return B
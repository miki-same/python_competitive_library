def extgcd(a,b):
    """
    拡張ユークリッドの互除法
    
    Parameters
    ----------
    a: int
    b: int
        
    Returns
    -------
    g:
        gcd(a,b)
    x,y:
        ax+by=gを満たすx,y
    """

    if b==0:
        return a,1,0
    else:
        r,p=a//b,a%b
        g,x,y=extgcd(b,p)
        return g,y,x-r*y

def crt(B,M):
    """
    中国剰余定理

    Parameters
    ----------
    B: list
    M: list
        
    Returns
    -------
    r: int
    z: int
        x≡B[i] (mod m[i]), ∀i∈{0,1,...,n-1}を解き、
        x≡r (mod z) と表せるr,zを返す
    """
    r,z=0,1
    for b,m in zip(B,M):
        b1,m1=r,z
        b2,m2=b,m
        g,x,y=extgcd(m1,m2)
        x,y=(b2-b1)//g*x,(b2-b1)//g*y
        if b1%g!=b2%g:
            return (0,0)
        a=(m1*x+b1)%(m1*m2//g)
        r,z=a,m1*m2//g
    return r,z
def z_algorithm(S):
    N=len(S)
    A=[0]*N
    i=1;j=0
    while i<N:
        while(i+j<N and S[j]==S[i+j]):
            j+=1
        A[i]=j
        if j==0:
            i+=1
            continue
        k=1
        while i+k<N and k+A[k]<j:
            A[i+k]=A[k]
            k+=1
        i+=k
        j-=k
    return A
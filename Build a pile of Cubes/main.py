def find_nb(m):
    m1=0
    n=0   
    while m1<m:
        m1=m1+n**3
        n+=1
    if m1==m:
        return (n-1)
    if m1!=m:
        return (-1)

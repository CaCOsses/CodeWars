def tower_builder(n_floors):
    i=0
    b=1
    a=([])    
    while i<n_floors:
        e=(2*n_floors-1)//2      
        c=(e-i)*" "+b*"*"+(e-i)*" "
        b=b+2
        i=i+1
        a.append(c)
    return(a)
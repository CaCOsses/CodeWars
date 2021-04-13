def decipher_this(string):
    b="ABCDEFGHIJKLMNOPQRSTUVWXYZ      abcdefghijklmnopqrstuvwxyz"
    a=string.split()
    e=""
    for i in (a):
        c=""
        for o in (i):
            if o.isdigit()==True:
                c=c+o
        if len(i)-len(c)<1:       
            d=b[int(c)-65]+" "
        if len(i)-len(c)==1: 
            d=b[int(c)-65]+i[-1]+" "  
        if len(i)-len(c)==2: 
            d=b[int(c)-65]+i[-1]+i[len(c)]+" "
        if len(i)-len(c)>2:
            d=b[int(c)-65]+i[-1]+i[len(c)+1:len(i)-1]+i[len(c)]+" "
        e=e+d 
    return (e.rstrip(" "))
def dashatize(num):
    if num==None:
        return("None")
    if num<0:
        num=-1*num  
    a=str(num)
    b=""
    c=0
    for i in a:
        c=+1+c
        if int(i)%2==0:
            b=b+i         
        else:
            if c>(len(a)-1):
                b=b+"-"+i
            elif int(a[c])%2!=0:
                b=b+"-"+i             
            elif int(a[c])%2==0: 
                b=b+"-"+i+"-"
    return(b.strip("-"))
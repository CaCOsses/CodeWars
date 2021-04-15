def data_reverse(data):
    a=int(len(data)/8)
    c=([])
    for i in range (a,0,-1):
        b=data[8*(i-1):8*i]
        if b!=[]:
            c=c+b
    return(c)
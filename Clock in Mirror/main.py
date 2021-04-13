def what_is_the_time(time_in_mirror):
    a = int (time_in_mirror[:2])
    b = int (time_in_mirror[-2:])   
    b = b / 60  
    c = a + b - 12

    if  a > 10:
        c = 12 - c
    else:
        c = -c
    
    a = int (c // 1)
    b = int(round(c % 1 * 60))
    r1 = str(a)
    r2 = str(b)

    if a < 10:
        r1 = '0' + r1
    if b < 10:
        r2 = '0' + r2
        
    r = r1 + ':' + r2
    return(r)
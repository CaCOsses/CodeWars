# n : number of intervals
def len_curve(n):
    # your code
    i = 0
    x2 = 0.0
    x1 = 0.0
    L = 0.0
    
    while n > i:
        x1 = x2
        y1 = x1 * x1
        x2 = x1 + 1/n
        y2 = x2 * x2
        L = ((y2-y1)**2 + (x2-x1)**2)**0.5 + L 
        i = i + 1
    return(round(L, 9))
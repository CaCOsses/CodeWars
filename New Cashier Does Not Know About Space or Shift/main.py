def get_order(order):
    i = 0
    c = 0
    r=""
    a =  ["burger", "fries", "chicken", "pizza", "sandwich", "onionrings", "milkshake", "coke"]
    
    while i < len(a):
        c = order.count(a[i])
        if c > 0:
            r = r + (order[order.find(a[i]):order.find(a[i])+len(a[i])] + " ") * c
        i = i + 1
    r = r.title()
    
    return(r[:-1])
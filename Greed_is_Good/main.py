def score(dice):
    i = 1
    c = 0
    r = 0
    while i <= 6: 
        c = dice.count(i)
        if c > 2 and i != 1:
            r = i * 100 + r
            c = c - 3
        if c > 2 and i == 1:
            r = i * 1000 + r
            c = c - 3
        if c < 3 and i == 1:
            r = c * 100 + r        
        if c < 3 and i == 5:
            r = c * 50 + r 
        i = 1 + i
    return (r)
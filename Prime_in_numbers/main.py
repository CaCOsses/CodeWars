def primeFactors(n):
    r=""
    i = 2

    while n > i:
        r1 = 0
        i1 = 0
        if es_primo(i) == False:
            i = i + 1
        while n % i == 0:
            i1 = i
            n = n / i1
            r1 =  1 + r1
        if r1 > 1 and i1 > 0:
            r = r + "(" + str(i) + "**" + str(r1) + ")"
        elif i1 > 0:
            r = r + "(" + str(i) + ")"
        i = i + 1
    print(r)
    return(r)
                
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
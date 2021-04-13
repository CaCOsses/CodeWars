def solution(s):
    i = 0
    r = ""
    while i < len(s):
        if s[i].isupper() == True:
            r =  r + " "
        r =  r + s[i]
        i = i + 1
    return(r)
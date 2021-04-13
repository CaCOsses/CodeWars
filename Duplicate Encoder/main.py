def duplicate_encode(word):
    a=""
    word=word.lower()
    i=0
    b=""
    while i<len(word):
        if word.count(word[len(word)-1-i])>1:
            a=")"
        else:
            a="("        
        b=a+b
        i+=1
    return(b)
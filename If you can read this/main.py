def to_nato(words):
    dictionary = {'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    words = words.upper()
    c = 0
    r = ""
    while c< len(words):
        if ord(words[c]) < 65 or ord(words[c]) > 90:
            if ord(words[c]) == 32:
                a = 1
            else:
                r = r + words[c] + " " 
        else:
            r = r + str(dictionary.get(words[c])) + " " 
        c = c + 1
    r = r [:-1]
    return(r)
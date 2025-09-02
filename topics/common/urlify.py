def urlify(s):
    res = ""
    i = 0 
    while i<len(s):
        if s[i] == ' ':
            res += "%20"
        else:
            res += s[i]
        i += 1

    return res

print(urlify("hello guys, how are you"))
string = "aeiou"

def count_vowels(string):
    count = 0
    i = 0
    while i<len(string):
        ch = string[i].lower()
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            count +=1
        i+=1
    return count

print(count_vowels(string))

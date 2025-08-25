s = "a,z,y,x,y,y,z,a,a,a,a"
q = "z,d,x,a,y"

hashlist = dict()

for ch in s:
    if ch == ',':
        continue
    ascii_val =ord(ch)
    index = ascii_val - 97
    hashlist[index]= hashlist.get(index,0)+1

for ch in q:
    if ch == ',':
        continue
    ascii_val = ord(ch)
    index = ascii_val-97
    hashlist[index]= hashlist.get(index,0)+1

    
    print(f"{ch}:{hashlist.get(index)}")
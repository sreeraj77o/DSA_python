def count_substring(s, sub):
    count = 0
    i = 0
    while i + len(sub) <= len(s):
        j = 0
        match = True
        while j < len(sub):
            if s[i+j] != sub[j]:
                match = False
                break
            j += 1
        if match:
            count += 1
        i += 1
    return count

print(count_substring("ababab","aba"))  # 2

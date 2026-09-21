def inverte(s):
    if s == "":             
        return s
    return inverte(s[1:]) + s[0]

print(inverte("Python"))
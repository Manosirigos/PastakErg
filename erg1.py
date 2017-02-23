k = raw_input("type something>> ")
n = list(k)
m = len(n)
i= 0
while i <= (m-1):
    if i in range(m-1):
        if n[i] == "!":
            n[i] = ""
    i += 1
print ''.join(n)

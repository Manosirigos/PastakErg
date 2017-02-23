k = raw_input("type something>> ")
n = list(k)
m = len(n)
i= 0
l= 0
while i <= (m):
    if i in range(m):
        if n[i] == "0":
            n[i] = ""
            l += 1
    i += 1
p = ''.join(n)
r = list(p)
for i in range(l):
    r.append(0)
print (r)


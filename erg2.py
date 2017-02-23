k = raw_input("type something>> ")
n = list(k)
m = len(n)
i = 0
p = 0
if n[0] == "(":
    while i <= (m-1):
        if n[i] == "(":
            p = p + 1
        else:
            if n[i] == ")":
                p = p - 1
        i += 1
    print (p)           
    if p == 0:
        print('TRUE')
    else:
        print('FALSE')
else:
    print('FALSE')

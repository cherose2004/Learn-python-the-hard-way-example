m = [1,1]
n = [1]
#print(n)
print("{0:^81}".format(str(1)))
for i in range(1,15):
    for j in range(i-1):
        n[j+1] = m[j] + m[j+1]
    n.append(1)
    m = n[:]
#    print(n)

    l = len(n)
    s = []
    p = []
    for i in range(l):
        s.append(str(n[i]))
    p = "   ".join(s)
    print("{0:^81}".format(p))
    
    

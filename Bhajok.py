q = int(input())
for i in range(q):
    w = int(input())
    print("Case",i + 1,end = "")
    print(":",end = " ")
    for e in range(1,w + 1):
        if (w % e == 0):
            print("",e,end = "")
print()
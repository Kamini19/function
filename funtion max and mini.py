def rty(a):
    i=1
    p=a[0] 
    while i<len(a):
        if a[i]>p:
            p=a[i]
        i=i+1
    print(p)
rty([1,2,3,3,4])


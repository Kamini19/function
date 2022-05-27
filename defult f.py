# def f(name,msg="gud morning"):
#     print("hallow",name +',' + msg)
# f("tanu")
# f("kamini","haow are u")

    
# def a(name,msg="gud aftoonun"):
#     print("hi",name+', ' +msg)
# a("insha")
# a("khushbu","hou are u")



a=[[4,3,2],[5,6,7],[9,10,12]]
i=0
sum=0
z=2
while i<len(a):
    j=0
    while j<len(a[i]):
        if(i==0):
            sum=sum+a[i][j]
        else:
            sum=sum+a[i][z]
            break
        j=j+1
    i=i+1
print(sum)


n=int(input())
a=0
b=1
while(n>0):
    if(n==1):
        print(a)
        break
    print(a,"",b,end="  ")
    a=a+b
    b=a+b
    n-=2

n=int(input("Enter the size of list : "))
ar=list(map(int,input("Enter the numbers of list : ").strip().split()))[:n]
print("Positive numbers in the list are : ")
for i in range(n):
    if ar[i]>=0:
        print(ar[i])


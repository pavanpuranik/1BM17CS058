a=[]
n=int(input("Enter the number of elements"));
for i in range(0,n):
    b=int(input("Enter number"))
    a.append(b)

c=int(input("Enter element to be searched"))
for i in a:
    if(i==c):
        print("Element found");
        break
else:
    print("Not found");

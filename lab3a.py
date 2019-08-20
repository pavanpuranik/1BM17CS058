a=int(input("Enter a number"))
list=[]
for i in range(1,a+1):
      if(a%i==0):
          list.append(i)

print(list)


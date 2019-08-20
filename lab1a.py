list=[]
n=int(input("enter the number of elements:"))
print("enter the elements")
for i in range(n):
 a=int(input())
 list.append(a)

y=[] 
for j in range(len(list)):
  if j%2==0:
    y.append(list[j])

for k in y:
 print(y)  

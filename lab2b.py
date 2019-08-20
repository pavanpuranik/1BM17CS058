
def rev1(str):

    str2=" "
    list1=str.split()
    list1.reverse()
    
    print(str2.join(list1))
    
    

def rev2(str):
    str3=""
    list2=str.split()
    
    for i in list2:
        str3+=i[::-1]
        str3+=" "
    print(str3)
    
    

str=input("Enter a string")
rev1(str)
rev2(str)

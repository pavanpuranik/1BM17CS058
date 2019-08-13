fib = [ 0,1]
a=int(input("Enter a number"));
for i in range ( 2, a):
     fib.append( fib[i-2] + fib[i-1])
print( fib)     

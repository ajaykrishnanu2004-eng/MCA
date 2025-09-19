a=float(input("enter the first number :"))
b=float(input("enter the second number:"))
c=input("choose an arithmetic operation:\n 1.addition\n 2.subtraction:\n 3.division:\n 4.multipiication:\n 5.exponential\n 6.floor division\n 7.modulo")
if c="1":
   d=a+b
elif c="2":
     d=a-b
elif c="3":
     d=a/b 
elif c="4":
     d=a*b
elif c="5":
     d=a**b
elif c="6":
     d=a//b
elif c="7":
     d=a%b
else:
     print("invalid option")
print("the result of the arithmetic operation is:",d)        

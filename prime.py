lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
for i in range(lower,upper+1):
    if i>1:
       for j in range(2,int(i**0.5)+1):
           if i%j==0:
              break:
           else:
                print(i)

#complex calculator
from cgitb import reset


x = input("enter the first number" )
y = input("enter the second number" )
p = input("enter the operator.eg(+,-,/,*,%.) ")
if p == '+':
    result = int(x) - int(y)
    print(x,p,y, "=" ,result)
elif p =='-':
    result = int(x) - int(y)
    print(x,p,y, "=" ,result)
elif p =='*':
    result = int(x) * int(y)
    print(x,p,y, "=" ,result)
elif p =='/':
    result = int(x) / int(y)
    print(x,p,y, "=" ,result)
elif p =='%':
    result = int(x) % int(y)
    print(x,p,y, "=" ,result)
else :
    print("invalid operator")

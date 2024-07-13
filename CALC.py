def add(a,b):
    return(a+b)
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    if(b==0):
        return("b cannot be 0")
    return(a/b)
def mod(a,b):
    return(a%b)
def pow(a,b):
    return(a**b)
n1=int(input("enter the value a:"))
n2=int(input("enter the value b:"))
while True:
    choice=input("Enter your choice (+, -, *, /, %, ^):")
    if(choice=='+'):
        res=add(n1,n2)
        print("result:",res)
        break
    elif(choice=='-'):
        res=sub(n1,n2)
        print("result:",res)
        break
    elif(choice=='*'):
        res=mul(n1,n2)
        print("result:",res)
        break
    elif(choice=='/'):
        res=div(n1,n2)
        print("result:",res)
        break
    elif(choice=='%'):
        res=mod(n1,n2)
        print("result:",res)
        break
    elif(choice=='^'):
        res=pow(n1,n2)
        print("result:",res)
        break
    else:
        print("invalid choice!, please enter any of the following choices:+,-,*,/,^,%")





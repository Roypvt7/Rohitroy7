print ("Enter any two number ")
a= int (input ("Enter a"))
b= int (input ("Enter b"))
       
def add(a,b) :
    return a+b
def sub (a,b) :
    return a-b
def mul (a,b) :
    return a*b
def div (a,b) :
    return a/b
print ("1 = Addition")
print ("2 = Subtraction" )
print ("3 = Multiplication" )
print ("4 = Division")
choice = int (input ("Enter your choice"))

if choice -- 1:
    print (add (a,b))
elif choice == 2:
    print (sub (a,b))
elif choice == 3:
    print (mul (a,b))
elif choice == 4:
    print (div (a,b))
else :
    print ("Wrong option")

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select Operation!!")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
sel=int(input("select 1,2,3,4:"))
x=int(input("enter 1st input value:"))
y=int(input("enter 2nd input value:"))
if sel==1:
    print("Addition:",add(x,y))
elif sel==2:
    print("Subtraction:",subtract(x,y))
elif sel==3:
    print("Multiplication:",multiply(x,y))
elif sel==4:
    print("Division:",divide(x,y))
else:
    print("Invalid choice")

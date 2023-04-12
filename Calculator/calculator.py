# This is a python script for Basic Calculator
#todo : remove hard coding practices
#todo : will use more functions for each action

# Input the 1st value
x = int(input("Enter the 1st value : "))

# Input the 2nd value
y = int(input("Enter the 2nd value : "))

# Function for Addition
def Addition(x,y):
    print(x," + ",y," = ",(x+y))

# Function for Subtraction
def Subtraction(x,y):
    print(x," - ",y," = ",(x-y))

# Function for Multiplication
def Multiplication(x,y):
    print(x," * ",y," = ",(x*y))

# Function for Division
def Division(x,y):
    print(x," / ",y," = ",(x/y))

# Call a funtion
#? Addition(x,y)

# Input the required function (s,a,d,m)
c = input("Enter 'a' for Addtion, 's' for Subtraction, 'm' for Multiplication, 'd' for Division : ")

if c == "a" :
    Addition(x,y)
elif c == "s" :
    Subtraction(x,y)
elif c == "d" :
    Division(x,y)
elif c == "m" :
    Multiplication(x,y)
else :
    print("Invalid value")

print("Do want to perform next calculation?")
b = input("Choose 'y' for Yes and 'n' for No : ")


#
#
#Practical 1
#
#
factors=[]
num=int(input("Enter the Number"))
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print(factors)
#
#
#Practical 2
#
#
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):                 
    for j in range(rows - i):                
        print(" ", end="")                   

    num = 1
    for k in range(1, i + 1):                
        print(num, end=" ")                  
        num = num * (i - k) // k            
    print()                                  
#
#
#Practical 3
#
#

import math

num1=int(input("Enter the first Number"))
num2=int(input("Enter the second Number"))
def hcf():
    print("HCF: ", math.gcd(num1,num2))

def lcm():
    
    print("LCM: ",math.lcm(num1,num2))
               
hcf()
lcm()
#
#
#Practical 4
#
#
inputno=int(input("Enter the no. of terms of series upto which u want fibonacci series: "))
def fibonacci():
    a=0
    b=1
    i=0
    while i<inputno:
        print(a, end=' ')
        a,b=b,a+b
        i=i+1

fibonacci()
#
#
#Practical 5
#
#

def menu():
        print("\n 1. ADD")
        print("\n 2. SUB")
        print("\n 3. MUL")
        print("\n 4. DIV")
        print("\n 5. PALINDROME")
        print("\n 6. MEAN")
        print("\n 7. CHECK LEAP YEAR")
        print("\n 8. SIMPLE INTEREST")
        print("\n 9. PROFIT OR LOSS")
        print("\n 10.AREA OF SQUARE")
        print("\n 11.AREA OF RECTANGLE")
        print("\n 12.AREA OF TRIANGLE")
        
        
menu()
option=int(input("\n Enter the option"))
        


def add():
    n1=int(input("Enter num 1:"))
    n2=int(input("Enter num 2:"))
    print("Addition: ", n1+n2)

def sub():
    n1=int(input("Enter num 1:"))
    n2=int(input("Enter num 2:"))
    print("Substraction: ", n1-n2)

def mul():
    n1=int(input("Enter num 1:"))
    n2=int(input("Enter num 2:"))
    print("Multiplication: ", n1*n2)

def div():
    n1=int(input("Enter num 1:"))
    n2=int(input("Enter num 2:"))
    print("Division: ", n1/n2)

def palindrome():
    data=input("Enter the Data")
    revdata=data[::-1]
    if data==revdata:
        print("Palindrome")
    else:
        print("Not Palindrome")

def mean():
    nos=[]
    count=0
    n=int(input("Enter the no. of numbers"))
    for i in range(n):
          no=int(input("Enter the number"))
          nos.append(no)
          count=count+no
    print(nos)
    mean=count/n
    print("The mean of data is: ",mean)

def leapy():
    year=int(input("Enter the year: "))
    if year%4==0:
        print("Leap year")
    else:
        print("Not Leap year")

def proloss():
    sp=int(input("Enter the selling price"))
    op=int(input("Enter the original price"))
    diff=sp-op
    if diff>0:
        print("Profit")
    else:
        print("Loss")

def sinterest():
    p=int(input("Enter the Principle amount:"))
    r=int(input("Enter the Rate of interest:"))
    t=int(input("Enter the time duration:"))
    si=p*r*t/100
    print("The Simple Interest is: ",si)

def asquare():
    l=int(input("Enter Length"))
    area=l**2
    print("Area of square",area)

def arectangle():
    l=int(input("Enter Length"))
    b=int(input("Enter Breadth"))
    area=l*b
    print("Area of Rectangle",area)

def atriangle():
    l=int(input("Enter Length"))
    b=int(input("Enter Breadth"))
    area=l*b/2
    print("Area of Triangle",area)

match option:
        case 1:
                add()
        case 2:
                sub()
        case 3:
                mul()
        case 4:
                div()
        case 5:
                palindrome()
        case 6:
                mean()
        case 7:
                leapy()
        case 8:
                sinterest()
        case 9:
                proloss()
        case 10:
                asquare()
        case 11:
                arectangle()
        case 12:
                atriangle()
        case _:
                print("Invalid Option")     

    

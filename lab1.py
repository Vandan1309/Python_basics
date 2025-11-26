#
#
#
#Practical 1
#
#
#
a=1
b=True
c="Vandan"
d=2.4
e={"1","2","3"}
f=2+3j
g=["2","3","4","5"]
h={ "name" :"Vandan", "age" : 36 }
i=("2","3","4")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(".")
print(".")
print(".")
#
#
#
#Practical 2
#
#
#
num1=int(input("Enter the first no."))
print(num1)
num2=int(input("Enter the second no."))
print(num2)
operator=input("Enter the operation u want to perform")
print(operator)

if(operator=="+"):
    print("The sum of both the nos. is:", num1+num2)

elif(operator=="-"):
    print("The difference of both the nos. is:", num1-num2)

      
elif(operator=="*"):
    print("The product of both the nos. is:", num1*num2)

elif(operator=="/"):
    print("The quotient of both the nos. is:", num1/num2)

elif(operator=="%"):
    print("The remainder of both the nos. is:", num1%num2)

elif(operator=="^"):
    print("The value of x to the power of y is:", num1**num2)

else:
    print("Invalid Operation")
print(".")
print(".")
print(".")
#
#
#
#Practical 3
#
#
#
no1=int(input("Enter the first no."))
no2=int(input("Enter the second no."))
no3=int(input("Enter the third no."))
print("The largest no. among these three entered no. is: ")
print(max(no1,no2,no3))
print(".")
print(".")
print(".")
#
#
#
#Practical 4
#
#
#
inputstring=input("Enter the input String") 

print(f"Original string: '{inputstring}'")
print(f"Length string: '{len(inputstring)}'")
print(f"Upper s:'{inputstring.upper()}'")
print(f"Lower s:'{inputstring.lower()}'")
print(f"Caps s:'{inputstring.capitalize()}'")
print(f"Strip s:'{inputstring.strip()}'")
print(f"Swapcase s:'{inputstring.swapcase()}'")
print(f"Checking if numeric: '{inputstring.isnumeric()}'")
print(f"Checking if alphanumeric: '{inputstring.isalnum()}'")
print(f"Checking if alphabet: '{inputstring.isalpha()}'")
print(".")
print(".")
print(".")
#
#
#
#Practical 5
#
#
#
instring=input("Enter the input String")
splitted_list=instring.split(" ")
print(splitted_list)
print("The no. of words in the given string is:",len(splitted_list))
print(".")
print(".")
print(".")
#
#
#
#Practical 6
#
#
#
userinstring=input("Enter the input string:" )
if(len(userinstring)>13):
    print("The four characters at the index values: 1,2,5,11 are: {}, {}, {}, {}".format(userinstring[1],userinstring[2],userinstring[5],userinstring[11]))
    print("The Sliced characters from index values 3 to 5 is : ", userinstring[3:5])
    print("The alternate characters of the input string are : ", userinstring[:len(userinstring):2])
    print("The alternate characters of the input string are : ", userinstring[::-1])
print(".")
print(".")
print(".")

    

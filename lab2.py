#
#
#
#Lab 2
#
#
#
#Practical 1: Even/Odd
#
#
#
no=int(input("Enter the no.: "))
if no%2==0:
       print("The No. is even")
else:
    print("The No. is Odd")
#
#
#
#Practical 2: Palindrome
#
#
#
input_val=input("Enter the No. or String")
rev_val=input_val[::-1]
if input_val==rev_val:
    print("Palindrome")
else:
    print("Not Palindrome")
#
#
#
#Practical 3: Vowel
#
#
#
instring=input("Enter the String")
x=instring.lower()
for i in x:
    if i in 'aeiou':
        print("Vowel Found:",i)
#
#
#
#Practical 4: Fibonacci
#
#
#
n=int(input("Enter the no. of terms upto which u would like ur fibonacci series: "))
t1=0
t2=1
print("0")
print("1")

for i in range(2,n+1,1):
    next_term=t1+t2
    print(next_term)
    t1=t2
    t2=next_term

    
    
   

       
       
       
       
       
       
       
       

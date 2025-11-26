"""
#
#
#
#Practical a
#
#
#
list1=[1,2,2,3,4]
print(list1)
list1.append(5)
print(list1)
list1.remove(3)
print(list1)
count=0
n=int(input("Enter the no. u want to count in the list"))

for i in list1:
    if(i==n):
        count=count+1
print("The entered no. comes in the list following times:")
print(count)
#
#
#
#Practical b
#
#
"""
#
d1={"brand" : "Ford" , "model" : "Mustang" , "Year" : 2000}
d2=dict(name="Ram" , age=30)

print(d1["model"])
print(d2.get("name"))

d1["color"]="red"
d1["Year"]=2005

del d1["brand"]
rem=d1.pop("model")
print(rem)

last=d1.popitem()
print(last)

for key,value in d1.items():
    print({key},":" ,{value})
d={"a":1,"b":2}
d.clear()
print(d)

od={"a":1,"b":2}
cd=od.copy()
print(cd)

keys=['apple','banana']
nd=dict.fromkeys(keys,0)
print(nd)
md={'name':'ved','age':20}
nm=md.get('name')
city=md.get('city','unknown')
print(nm)
print(city)

md={'a':1,'b':2}
iv=md.items()
print(list(iv))
"""
#
#
#
#Practical c
#
#
#

name1=input("Enter the name of the student")
marksa1=input("Enter the marks of the student in maths")
marksa2=input("Enter the marks of the student in english")
marksa3=input("Enter the marks of the student in biology")
marksa4=input("Enter the marks of the student in botany")
marksa5=input("Enter the marks of the student in python programming")
    
name2=input("Enter the name of the student")
marksb1=input("Enter the marks of the student in maths")
marksb2=input("Enter the marks of the student in english")
marksb3=input("Enter the marks of the student in biology")
marksb4=input("Enter the marks of the student in botany")
marksb5=input("Enter the marks of the student in python programming")

name3=input("Enter the name of the student")
marksc1=input("Enter the marks of the student in maths")
marksc2=input("Enter the marks of the student in english")
marksc3=input("Enter the marks of the student in biology")
marksc4=input("Enter the marks of the student in botany")
marksc5=input("Enter the marks of the student in python programming")



students={
        "s1" : {
        "name" : name1,
        "maths :" : marksa1 ,
        "english": marksa2 ,
        "biology" : marksa3 ,
        "botany" : marksa4 ,
        "Python programming" : marksa5
        },
        
        "s2" : {
        "name" : name2,
        "maths :" : marksb1 ,
        "english": marksb2 ,
        "biology" : marksb3 ,
        "botany" : marksb4 ,
        "Python programming" : marksb5
        },
        
        "s3" : {
        "name" : name3,
        "maths :" : marksc1 ,
        "english": marksc2 ,
        "biology" : marksc3 ,
        "botany" : marksc4 ,
        "Python programming" : marksc5
        }
        }

print(students)

#
#
#
#Practical d
#
#
#
"""
string1=input("Enter the numbers for first list" )
string2=input("Enter the numbers for second list")
l1=list(string1)
l2=list(string2)
print("List 1: ")
print(l1)
print("List 2: ")
print(l2)
l1.extend(l2)
l3=l1
l=len(l3)
print(l3)
"""
#
#
#
mid=int(l/2)

while mid>1:
    for i in range(0,mid):
        
        print(mid)
        mid=int(mid/2)
         

    print("The broken list 1: ")
        for j in range(0,i):
            print(l3[j])
    for i in range(mid+1,l):
        print("The broken list 2: ")
        for k in range(mid+1,l):
            print(l3[k]

#
#
#
#Practical e
#
#
#
array1=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]]
array2=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]]
matrixsum=[]
print("Matrix before replacement: ")
for i in array1:
   print(i)
#
#
#
array1[0][1][2]=16
print("Matrix after replacement: ")
for i in array1:
    print(i)
#
#
#
for i in range(3):
    print("3x3 array extracted no.: ",i+1)
    m3x3=array1[i]
    for j in m3x3:
        print(j)

#
#
#
total=0
for i in array1:
    for j in i:
        for k in j:
            total+=k
print("total: ", total)

"""


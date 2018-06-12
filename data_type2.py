#Q.1- Write a program to create a tuple with different data types and find the length of tuples
tup1=(1,'tomato',4.0,3+2j)
print("tupple is:",tup1)
print("length of tupple is:",len(tup1),"\n\n")
print(10*"*")


#Q.2-Find largest and smallest elements of a tuples.
tup2=(2,7,3,1,0,66,24,91,43)
print("tupple is:",tup2)
print("largest element is:",max(tup2))
print("smallest element is:",min(tup2),"\n\n")
print(10*"*")


#Q.3- Write a program to find the product of all elements of a tuple.
numbers=(3,2,2,5,4)
print("elements of tupple are:",numbers)
prod=1
for i in numbers:
        prod *= i
print("product of all elements of tuple is :",prod,"\n\n")
print(10*"*")


#Q.4-Create two sets using user defined values.
x1=input("enter first element of set1: ")
y1=input("enter second element of set1: ")
z1=input("enter third element of set1: ")
set1={x1,y1,z1}
x2=input("enter first element of set2: ")
y2=input("enter second element of set2: ")
z2=input("enter third element of set2: ")
set2={x2,y2,z2}
print("elements of set1 are:",set1)
print("elements of set2 are:",set2,"\n\n")
print(10*"*")


#Q.5-Calculate difference between two sets
set1={2,7,2,9,3}
set2={1,3,7,40}
print("elements of set1 are:",set1)
print("elements of set2 are:",set2)
set3=set1-set2
print("difference of set1-set2=",set3)
print("difference of set2-set1=",set2-set1,"\n\n")
print(10*"*")



#Q.6-compare two sets.
set1={2,4,6,1,3,5,9}
set2={3,5,3,9}
print("elements of set1 are:",set1)
print("elements of set2 are:",set2)
print("Is set1 superset of set2?")
x=set1>=set2
print(x,"\n\n")
print(10*"*")



#Q.7-Intersection of two sets.
set1={2,'right',3,5,4,9}
set2={3,1,6,7,'right'}
print("elements of set1 are:",set1)
print("elements of set2 are:",set2)
print("intersection of above two sets=",set1&set2,"\n\n")
print(10*"*")




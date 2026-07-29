import math 
lst1=[] 
lst2=[] 
n=int(input("Enter number of elements:")) 
print("Enter the Element in list 1:") 
for i in range(0,n): 
    x=int(input()) 
    lst1.append(x) 
print("The given elements in list1 are:") 
print(lst1) 
print("Enter the  elements in list2") 
for i in range(0,n): 
    y=int(input()) 
    lst2.append(y) 
print("The given Element in list2 are:") 
print(lst2) 
num=sum(x*y for x,y in zip(lst1,lst2)) 
print("The numberator is:") 
print(num) 
normx=sum(x**2 for x in lst1) 
normy=sum(y**2 for x in lst2) 
den=math.sqrt(normx)*math.sqrt(normy) 
sim=num/den 
print("The cosine similarity is") 
print(sim)
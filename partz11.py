import math 
lst1=[] 
lst2=[] 
n=int(input("Enter number of elements: ")) 
print("Enter the elements in list 1:") 
for i in range(n): 
    x=int(input()) 
    lst1.append(x) 
print("The given elements in list1 are:") 
print(lst1) 
print("Enter the elements in list 2:") 
for i in range(n): 
    y=int(input()) 
    lst2.append(y) 
print("The given elements in list2 are:") 
print(lst2) 
num=sum(x*y for x,y in zip(lst1, lst2)) 
print("The numerator is:") 
print(num) 
normx=sum(x**2 for x in lst1) 
normy=sum(y**2 for y in lst2) 
Page | 23  
 
den=math.sqrt(normx) * math.sqrt(normy) 
sim=num/den 
print("The cosine similarity is:") 
print(sim)
import matplotlib.pyplot as plt 
lst=[] 
n=int(input("Enter range")); 
print("Enter the Elements") 
for i in range(0,n): 
    ele=int(input()) 
    lst.append(ele) 
print("user list is",lst) 
 
lst.sort() 
print("sorted list is",lst) 
half=n/2 
if(half % 2==0): 
    q1=(lst[n//4-1]+lst[n//4])/2 
    q3=(lst[3*n//4-1]+lst[3*n//4])/2 
else: 
    q1=lst[n//4] 
    q3=lst[3*n//4] 
 
print("The first Quartile Q1",q1) 
print("The third Quartile Q3",q3) 
iqr=q3-q1 
print("the inter quartile range is:",iqr) 
lb=q1-(1.5*iqr) 
ub=q3+(1.5*iqr) 
out=[] 
for x in lst: 
    if(x<lb)or(x>ub): 
        out.append(x) 
print('outlier data is',out) 
plt.boxplot(lst) 
plt.show()
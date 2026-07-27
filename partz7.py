import math 
lst=[] 
n=int(input("Enter number of elements:")) 
input("Enter the elements:") 
for i in range(0,n): 
    ele=int(input()) 
    lst.append(ele) 
print("The given List is:") 
print(lst) 
print("The sorted list is") 
lst.sort() 
print(lst) 
total=sum(lst) 
avg=total/n 
print("The mean of value is") 
print(avg) 
if(n%2)==0: 
    med=(lst[n//2-1]+lst[n//2])/2 
else: 
    med=lst[n//2] 
print("The median is") 
print(med) 
cnt=0 
num=lst[0] 
for i in lst: 
    curr_frequency=lst.count(i) 
    if(curr_frequency>cnt): 
        cnt=curr_frequency 
        num=i 
if cnt>1: 
    md=num 
else: 
    md=3*med-2*avg 
print("The mode is:") 
print(md) 
 
deviation=[(x-avg)**2 for x in lst] 
varience=sum(deviation)/n 
sd=math.sqrt(varience) 
print("The standard deviation is") 
print(sd)
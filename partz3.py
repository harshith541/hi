student={}
n=int(input("Enter number of key-value pairs:"))
for i in range(n):
    key=input(f"Enter key'{i+1}':")
    value=input(f"Enter value for'{key}':")
    student[key]=value
print("\nStudent Dictionary:",student)
search_key=input("\nEnter key to access its value:")
if search_key in student:
    print(f"Value of '{search_key}':",student[search_key])
else:
    print("Key not found")
print("\nAll Keys:",set(student.keys()))
print("\nAll Values:",set(student.values()))
print("\nAll Items:",set(student.items()))



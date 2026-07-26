def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
    print()
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(n,"is not a prime number")
                return
        print(n,"is a prime number")
    else:
        print(n, "is not a prime number")
num1=int(input("Enter number of terms(Fibonacci):"))
print("\nFibonacci Series:")
fib(num1)
num2=int(input("Enter number of Prime Check:"))
print("\nPrime Result:")
prime(num2)

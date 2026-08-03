def fast_power(base,exponent): 
    if exponent==0: 
        return 1 
    half=fast_power(base,exponent//2) 
    if exponent%2==0: 
        return half*half 
    else: 
        return base*half*half 
b=int(input("Enter base:")) 
e=int(input("Enter exponent(non-negative):")) 
if e<0: 
    print("Exponent must be non-negative") 
else: 
    result=fast_power(b,e) 
    print(f"{b}^{e}={result}")
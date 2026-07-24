def reverse(s):
    return s[::-1]
def palindrome(s):
    if s==s[::-1]:
        return"Palindrome"
    else:
        return"Not Palindrome"
def frequency(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    return freq
s=input("Enter string:")
print("\n1.Reverse")
print("2.Palindrome")
print("3.Frequency")
ch=int(input("Enter your choice:"))
if ch==1:
    print("Reverse:",reverse(s))
elif ch==2:
    print("Result:", palindrome(s))
elif ch == 3:
    print("Frequency:",frequency(s))
else:
    print("Invalid choice")

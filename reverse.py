n=int(input("Enter number"))
rev=0
while(i>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)
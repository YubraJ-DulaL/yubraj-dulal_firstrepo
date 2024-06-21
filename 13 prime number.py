f=0
for n in range(2,101,1):
    if n%2==0 or n%3==0 or n%4==0 or n%5==0 or n%6==0 or  n%7==0 or n%8==0 or n%9==0:
        f=f+1
    else:
        print(n)
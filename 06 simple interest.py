"""
WAP to calculate simple interest on the basis of following assumptions.
a.if balance is greater than 99999, interest is 7%
b.if balance is greater than or equal to 50000 and less than 100000 interest is 5%
c.if balance is less than 50000. interest is 3%
"""
principal=float(input("balance(principal)="))
time=float(input("Time=")) 
if principal>99999:
    rate=7 

elif principal>=50000:
    rate=5 

else:
    rate=3 
    
si = principal * time * rate / 100 #Simple Interest=p*t*r/100
print(f"rate={rate}")
print(f"Simple Interest={si}") #si=simple interest
print(f"Amount={principal+si}")

"""
WAP to calculate discount amount on the basis of following assumption.
if amount is greater or equal to 1000 then discount is 5%
if amount is less than 1000 then discount is 3%
"""
amount=float(input("amount="))
if amount>=1000:
    dis_per=5/100 #dis_per=discount percentage.
else:
    dis_per=3/100 #dis_per=discount percentage.

discount_amt=amount*dis_per #discount_amt=discount amount
print(f"discount Amount={discount_amt}")
print(f"Final Amount={amount-discount_amt}")
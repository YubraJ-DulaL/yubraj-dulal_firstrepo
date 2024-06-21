'''
WAP to calculate discount on the basis of the following assumption.
a.if purchased amount is greater than or equal to 5000, discount is 10%
b.if purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
c.if purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
d.if purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
e.if purchased amount is less than 2000, discount is 2%

'''
amount=float(input("purchase amount="))
if amount>=5000:
    dis_per=10/100 #disper=discount percentage.

elif amount>=4000:
    dis_per=7/100 #disper=discount percentage.
  
elif amount>=3000:
    dis_per=5/100 #disper=discount percentage.
 
elif amount>=2000:
    dis_per=3/100 #disper=discount percentage.
 
else:
    dis_per=2/100 #disper=discount percentage.
    
discount_amt=amount*dis_per #discount_amt=discount amount
print(f"discount amount={discount_amt}")
print(f"final amount={amount-discount_amt}") #amount after discount

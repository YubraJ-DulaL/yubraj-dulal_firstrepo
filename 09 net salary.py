"""
The rates of tax on gross salary are as shown below:
income TAx
Less than 10000 Nil
rs. 10000 to 19999 10%
rs. 20000 to 39999 15%
rs. 40000 to above 20%
Write a program to compute the net salary after deducting the tax.
"""
print("|-----------------------|")
salary=int(input("|Salary=")) #input the salary.
if salary>=40000:
    tax=20/100 #20%
elif salary>=20000:
    tax=15/100 #15%
elif salary>=10000:
    tax=10/100 #10%

amt=salary*tax #tax amount
print("|-----------------------|")
print(f"|Tax Amount={amt}\t|")
print("|-----------------------|")
print(f"|Net Salary={salary-amt}\t|")
print("|-----------------------|")



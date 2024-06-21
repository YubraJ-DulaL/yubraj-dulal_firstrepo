"""
WAP to calculate discount from the given assumption.
"""
amt=float(input("Amount="))
def dis():
    if amt >= 1000:
        #discount=5%
        dis=5/100
        discount=amt*dis #discount amount

    else:
        #discount=0%
        dis=0/100
        discount=amt*dis #discount amount

    print(f"Discount Amount={discount}")
    print(f"final Amount={amt-discount}")


dis()
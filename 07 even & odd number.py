"""
WAP to test whether a number is odd or even.
"""
number=int(input("Enter any number=")) #input the number
if number %2 == 0: #even number
    print(f"{number} is even number.")

else: #odd number
    print(f"{number} is odd number.")
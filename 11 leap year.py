# leap year is comes one time in 4 years.
#year is divisible by 4 & 400 but not divisible by 100 is called leap year.
year=int(input("Enter the year="))
if (year%4==0 and year%100 != 0) or year%400==0:
    print(f"{year} is a leap            year.")
else:
    print(f"{year} isn't leap year.")
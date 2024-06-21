number=float(input("Enter any number="))
number_1=number
sum=0
while number>10:
    remainder=number%10
    sum=sum+pow(remainder,3)
    remain_number=number-remainder
    number=remain_number/10
    if number<10:
        total=(sum+pow(number,3))
        if total==number_1:
            print(f"{number_1} is armstrong number.")
        else:
            print(f"{number_1} isn't armstrong number.")
number=float(input("Enter the number="))
number_1=number
digit=0
while number>10:
    remainder=number%10
    digit=digit*10+remainder
    number=number-remainder
    number=number//10
    if number<10:
        reverse_number=digit*10+number
        if reverse_number==number_1:
            print(f"{number_1} is palindrome number.")
        else:
            print(f"{number_1} isn't palindrome number.")
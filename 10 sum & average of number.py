def main(): #main function
    number = [11,12,13,14,15,16,17,18,19,20] # list of numbers
    sum = 0
    n = 0
    for i in range(0,10,1):
        sum = sum + number[i]
        n =n + 1
    print(f"sum={sum} n={n} Average={sum/n}") # value of sum, n and Average


main()
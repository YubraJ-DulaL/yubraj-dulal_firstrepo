# Calculator
print("|----------------------------|")
print("|Welcome to basic calculator.|")
print("|----------------------------|")
print("\n|========================================|")
print("|Operation:------------------------------|")
print("|==========|-----------------------------|")
print("|a. press 1 for Addition-----------------|")
print("|b. press 2 for Subtraction--------------|")
print("|c. press 3 for Multiplication-----------|")
print("|d. press 4 for Division-----------------|")
print("|e. press 5 for History------------------|")
print("|f. press 6 for Exit---------------------|")
print("|========================================|")
history=[]

def Menu():
    while True:
        result = 0
        try:
            key = int (input ( "Enter the option = " ))
            if key == 1:
                print ( "1 for addition" )
                print ( "|==================|" )
                first = float (input ("|first number = " ))
                second = float (input ("|second number = " ))
                print ( "|==================|" )
                result = first + second
                print ( "|=============================================|" )
                print (f"|Result = {result}" )
                history.append(history)
                print ( "|---------------------------------------------|")
                print ( "|Do you want to add again with result ?" )
                print ( "|---------------------------------------------|")
                option = input ( "|yes or no ? = " )
                print ( "|=============================================|" )
                if option == 'yes':
                    while option == 'yes':
                        third = float (input ( "|further number = " ))
                        result = result + third
                        print ( "|-------------------------------------------|" )
                        print (f"|Result = {result}" )
                        history.append(history)
                        print ( "|-------------------------------------------|" )
                        print ( "|Do you want to add again with result ?" )
                        print ( "|-------------------------------------------|" )
                        option = input ( "|yes or no ? = " )
                        print ( "|===========================================|" )
                        if option == 'yes':
                            continue
                        elif option == 'no':
                            break
                elif option == 'no':
                    break
                else:
                    print ( "Invalid input." )
            elif key == 2:
                print ( "2 for subtraction" )
                print ( "|==================|" )
                first = float (input ("|first number = " ))
                second = float (input ("|second number = " ))
                print ( "|==================|" )
                result = first - second
                print ( "|===========================================|" )
                print (f"|Result = {result}" )
                history.append(history)
                print ( "|-------------------------------------------|")
                print ( "|Do you want to subtract again with result ?" )
                print ( "|-------------------------------------------|")
                option = input ( "|yes or no ? = " )
                print ( "|===========================================|" )
                if option == 'yes':
                    while option == 'yes':
                        third = float (input ( "|further number = " ))
                        result = result - third
                        print ( "|-------------------------------------------|" )
                        print (f"|Result = {result}" )
                        history.append(history)
                        print ( "|-------------------------------------------|" )
                        print ( "|Do you want to subtract again with result ?" )
                        print ( "|-------------------------------------------|" )
                        option = input ( "|yes or no ? = " )
                        print ( "|===========================================|" )
                        if option == 'yes':
                            continue
                        elif option == 'no':
                            break
                elif option == 'no':
                    break
                else:
                    print ( "Invalid input." )
            elif key == 3:
                print ( "3 for multiplication" )
                print ( "|==================|" )
                first = float (input ("|first number = " ))
                second = float (input ("|second number = " ))
                print ( "|==================|" )
                result = first * second
                print ( "|===========================================|" )
                print (f"|Result = {result}" )
                history.append(history)
                print ( "|-------------------------------------------|")
                print ( "|Do you want to multiply again with result ?" )
                print ( "|-------------------------------------------|")
                option = input ( "|yes or no ? = " )
                print ( "|===========================================|" )
                if option == 'yes':
                    while option == 'yes':
                        third = float (input ( "|further number = " ))
                        result = result * third
                        print ( "|-------------------------------------------|" )
                        print (f"|Result = {result}" )
                        history.append(history)
                        print ( "|-------------------------------------------|" )
                        print ( "|Do you want to multiply again with result ?" )
                        print ( "|-------------------------------------------|" )
                        option = input ( "|yes or no ? = " )
                        print ( "|===========================================|" )
                        if option == 'yes':
                            continue
                        elif option == 'no':
                            break
                elif option == 'no':
                    break
                else:
                    print ( "Invalid input." )
            elif key == 4:
                print ( "4 for Division" )
                print ( "|==================|" )
                first = float (input ("|first number = " ))
                second = float (input ("|second number = " ))
                print ( "|==================|" )
                try:
                    result = first / second
                except:
                    print ( "Number isn't divisible by 0." )
                print ( "|===========================================|" )
                print (f"|Result = {result} " )
                history.append(history)
                print ( "|-------------------------------------------|")
                print ( "|Do you want to divide again with result ?" )
                print ( "|-------------------------------------------|")
                option = input ( "|yes or no ? = " )
                print ( "|===========================================|" )
                if option == 'yes':
                    while option == 'yes':
                        third = float (input ( "|further number = " ))
                        try:
                            result = result / third
                        except:
                            print ( "|-------------------------------------------|" )
                            print ( "|Number isn't divisible by 0." )
                        print ( "|-------------------------------------------|" )
                        print (f"|Result = {result} " )
                        history.append(history)
                        print ( "|-------------------------------------------|" )
                        print ( "|Do you want to divide again with result ?" )
                        print ( "|-------------------------------------------|" )
                        option = input ( "|yes or no ? = " )
                        print ( "|======================================|" )
                        if option == 'yes':
                            continue
                        elif option == 'no':
                            break
                elif option == 'no':
                    break
                else:
                    print ( "Invalid input." )
            elif key == 5:
                print ( "5 for History" )
                print (f"{history}")
            elif key == 6:
                print ( "6 for Exit" )
                return
            else:
                print ( "Invalid Operation." )

            print ( "|::::::::::::::::::::::::|" )
            print ( f"| final result = {result}" )
            print ( "|::::::::::::::::::::::::|" )
        except:
            print ( "Invalid Input." )
Menu ()
                
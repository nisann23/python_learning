
while True:  #the  program is inside a 'while True' loop to keep running 
    #until the user chooses 4 
    # 1. showing the options to the user

    print("Financial Calculator Menu")
    print("1. Calculate Simple Interest")
    print("2. Calculate Compound Interest")
    print("3. Calculate Loan Repayment")
    print("4. Exit")

    
    # 2. get the user's choice
    choice = input("Please enter an option (1-4): ")

    # 3. Process the choice using if/elif/else
    
    if choice == '1':
        #calculating simple interest
        print("\nSimple Interest Calculator ")
        # Get the necessary data using 'input'
        # changing the user's input from a string to a float so we can use it in our mathematical formula
        P = float(input("Enter Principal amount (P): "))
        r = float(input("Enter annual interest rate (e.g., 0.05): "))
        t = float(input("Enter time in years (t): "))
          
        # Formula: I = P * r * t
        interest = P * r * t
        
        print(f"The Simple Interest earned is: ${interest:.2f}")


    elif choice == '2':
        #COMPOUND INTEREST 
        print("\n Compound Interest Calculator")
        
        P = float(input("Enter Principal amount (P): "))
        r = float(input("Enter annual interest rate (e.g., 0.05): "))
        t = float(input("Enter time in years (t): "))
        
        # Formula (Compounded Annually): A = P * (1 + r)^t
        total_amount = P * (1 + r) ** t
        
        print(f"The total amount after {t} years is: ${total_amount:.2f}")

    elif choice == '3':
        #LOAN REPAYMENT
        print("\n Monthly Loan Repayment Calculator")
        
        P = float(input("Enter Loan Principal (P): "))
        annual_rate = float(input("Enter annual interest rate (e.g., 0.12): "))
        years = float(input("Enter loan term in years: "))

        monthly_rate = annual_rate / 12
        number_of_months = years * 12
        
        # Formula: M = P * [r(1+r)^n] / [(1+r)^n - 1]
        monthly_payment = P * (monthly_rate * (1 + monthly_rate) ** number_of_months) / ((1 + monthly_rate) ** number_of_months - 1)
        
        print(f"Your Monthly Loan Payment is: ${monthly_payment:.2f}")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break  # This command stops the 'while True' loop

    else:
        print("\nError: Invalid choice. Please enter a number between 1 and 4.")
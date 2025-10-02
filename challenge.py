# challenge

balance = 1000
withdrawals_today = 0
withdrawal_limit = 3

print("Welcome to the ATM!")

while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")


    if choice == "1":
        print(f"Your current balance is: ₱{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₱"))
        if amount > 0:
            balance += amount
            print(f"Deposited ₱{amount}. New balance: ₱{balance}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        if withdrawals_today >= withdrawal_limit:
            print("You have reached the daily withdrawal limit.")
        else:
            amount = float(input("Enter amount to withdraw: ₱"))
            if amount > 0 and amount <= balance:
                balance -= amount
                withdrawals_today += 1
                print(f"Withdrew ₱{amount}. New balance: ₱{balance}")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                print("Invalid withdrawal amount.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please select 1-4.")


    for i in range(withdrawal_limit - withdrawals_today):
        print(f"You can still withdraw {withdrawal_limit - withdrawals_today - i} more time(s) today.")
        break
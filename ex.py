
def show_balance(balance):
    print(f"Your account balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("That's not a valid amount!")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    new_balance = balance - amount
    if amount > balance:
        print("You have insufficient funds! Try Again!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0!")
        return 0
    else:
        print(f"You have successfully withdrawn: ${amount}")
        print(f"Your new account balance is: ${new_balance:.2f}")
        return amount


def main():
    print("Banking in python")
    balance = 0
    is_running = True

    while is_running:
        print("1.Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is an invalid choice!")

    print("Thank You! Have a nice day!")


main()

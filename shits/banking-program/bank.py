def show_balance(balance):
    print(f"\nYour balance is ₱{balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be deposited: ₱"))

    if amount < 0:
        print("Invalid amount.")
        return 0
    else:
        return amount
def withdraw(balance): 
    try:
        amount = float(input("Enter amount to be withdrawn: ₱"))
        if amount < 0:
            print("Invalid amount.")
            return 0
        elif amount > balance:
            print("Insufficient funds.")
            return 0
    except TypeError:
        print("Invalid")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("--------- BANKING PROGRAM ---------\n1. Show balance\n2.Deposit\n3.Withdraw\n4.Exit\n-------------- MENU --------------")

        try:
            choice = int(input("Enter your choice (1-4)\n--> "))
            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                balance += deposit()
            elif choice == 3:
                balance -= withdraw(balance)
            elif choice == 4:
                is_running=False
            else:
                print("Not a valid choice.\n")
        except ValueError:
            print("Error: Not a number.\n")
            
    print("\nThank you! Have a nice day!")

if __name__ == "__main__":
    main()
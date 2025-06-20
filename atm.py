# Global balance variable
balance = 1000.00

def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print(f"\n💰 Your current balance is: ₹{balance:.2f}")

def deposit_money():
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("⚠️ Amount must be greater than 0.")
        else:
            balance += amount
            print(f"✅ ₹{amount:.2f} deposited successfully.")
            check_balance()
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number.")

def withdraw_money():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("⚠️ Amount must be greater than 0.")
        elif amount > balance:
            print("❌ Insufficient balance.")
        else:
            balance -= amount
            print(f"✅ ₹{amount:.2f} withdrawn successfully.")
            check_balance()
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number.")

def atm():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            print("👋 Thank you for using our ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

# Run the ATM
atm()

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. Your new balance is ${self.balance}"
        else:
            return "Invalid amount. Please enter a positive amount to deposit."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"${amount} withdrawn. Your new balance is ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid amount. Please enter a positive amount to withdraw."

def main():
    atm = ATM()
    
    while True:
        print("\nATM Simulation")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
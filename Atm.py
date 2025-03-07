class Atm:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: Rs{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")#same like interpolation
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rs{amount} withdrawn successfully.")#for interpolation we will use this
        else:
            print("Invalid withdrawal amount or insufficient balance.")

def main():
    atm = Atm()
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: Rs"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: Rs"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
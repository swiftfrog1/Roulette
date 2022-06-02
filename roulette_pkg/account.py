from numpy import cov
class AccountInfo:
    # new player
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self):
        while True:
            if self.balance == 0:
                while True:
                    try:  
                        amount = float(input("Enter starting account balance: "))
                        if amount > 0.0:
                            self.balance += amount
                            print(f"\nAmount Deposited: ${amount:.2f}")
                            return self.balance
                        else:
                            print("Value must be greater than 0.")
                    except ValueError:
                        print(f"\nInvalid input. Enter a dollar amount.\n")
            elif self.balance > 0:
                print(f"\nCurrent Balance: ${self.balance:.2f}")
                while True:
                    add_money = input(
                        f"\nDo you want to add to the current balance of ${self.balance}?\nEnter (y) for yes, (n) to continue to roulette table: ")
                    if add_money.lower() == "y":
                        try:
                            add_amount = float(
                                input(f"Enter amount to add to the current balance of ${self.balance}: "))
                            self.balance += add_amount
                            print(f"\nAmount Deposited: ${add_amount:.2f}")
                            break
                        except ValueError:
                            print("\nInvalid Input")
                    elif add_money.lower() == "n":
                        print(
                            "\nYou have chosen NOT to add money to the existing account.")
                        break
                    else:
                        print(f"{add_money}: Invalid Input")
            break

    def loss(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\n-${amount:.2f} lost!!!")
        else:
            print(f"\nNo cash available")

    def win(self, amount):
        self.balance += amount
        print(f"\n+${amount:.2f} won!!!")

    def account_balance(self):
        return self.balance


''' ### USAGE ###
# enter 0 for new account or a number for existing account as parameter
acc = AccountInfo(0)
avail_cash = acc.deposit()
balance = acc.account_balance()
print(f"\nCurrent balance: ${balance:.2f}")
acc.loss(400)
balance = acc.account_balance()
print(f"\n Current balance: ${balance:.2f}")
acc.win(750)
balance = acc.account_balance()
print(f"\n Current balance: ${balance:.2f}") '''


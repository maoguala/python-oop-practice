class BankAccount:
    def __init__(self, owner, balance = 0):
        self.o = owner
        self.b = balance
    def despoit(self, amount):
        if amount > 0:
            self.b += amount 
            print(f"despoit {amount}$ successfully. Currnet balance is: {self.b}\n\n")
        else:
            print(f"despoit Failed. amount must be greater than 0$\n\n")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.b:
            self.b -= amount
            print(f"withdraw {amount}$ successfully. Currnet balance is: {self.b}\n\n")
        elif amount <= 0:
            print("Please Enter value greater than 0! \n\n")
        elif amount <= self.b:
            print(f"withdraw {amount}$ Failed. Insufficient balance. Currnet balance is: {self.b}\n\n")
    def get_balance(self):
        print(f"Current balance: {self.b}$\n\n")





name = input("Bank's accout name: ")

val = int(input("Despoit amount: "))

user_1 = BankAccount(name, val)

while True:
    sel = input("Please Enter Selection(With digit): (1)despoit (2)withdraw (3)Check Balance (4)Exit-> ")

    sel = int(sel)

    if sel == 1:
        amount = int(input("Enter amount to deposit: "))
        user_1.deposit(amount)
    elif sel == 2:
        amount = int(input("Enter amount to withdraw: "))
        user_1.withdraw(amount)
    elif sel == 3:
        user_1.get_balance()
    elif sel == 4:
        exit()
    else:
        print("Invalid Selection!")


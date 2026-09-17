class BankAccount:
    def __init__(self, owner, balance = 0):
        self.o = owner
        self.__b = balance
    def deposit(self, amount): # Transditional setter method
        if amount > 0:
            self.__b += amount 
            print(f"despoit {amount}$ successfully. Currnet balance is: {self.__b}\n\n")
        else:
            print(f"despoit Failed. amount must be greater than 0$\n\n")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__b:
            self.__b -= amount
            print(f"withdraw {amount}$ successfully. Currnet balance is: {self.__b}\n\n")
        elif amount <= 0:
            print("Please Enter value greater than 0! \n\n")
        elif amount <= self.__b:
            print(f"withdraw {amount}$ Failed. Insufficient balance. Currnet balance is: {self.__b}\n\n")
    def get_balance(self):
        print(f"Current balance: {self.__b}$\n\n")


name = input("Bank's accout name: ")

val = int(input("Despoit amount: "))

user_1 = BankAccount(name, val)

# print(user_1.__b) # Test, Because __b is private attribute, cause cannot not access directly


while True:
    sel = input("Please Enter Selection(With digit): (1)despoit (2)withdraw (3)Check Balance (4)Exit-> ")

    if not sel.isdigit():
        print("Please enter a valid number!\n")
        continue

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
        # exit()
        break
    else:
        print("Invalid Selection!")


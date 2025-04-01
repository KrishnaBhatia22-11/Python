class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} INR deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount("John Doe")
account.deposit(2000)
print(f"Current Balance: {account.get_balance()} INR")
print("1/23/SET/BCS/358")

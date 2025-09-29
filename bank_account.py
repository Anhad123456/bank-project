class BalanceException(Exception):
    pass

class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account created \n Name : {name} \n Balance : ${balance}")

    def getBalance(self):
        print(f"Account {self.name} balance is ${self.balance:.2f}")
        return self.balance
    
    def deposit(self, amount, isPrint = True):
        self.balance += amount
        if isPrint:
            print(f"Deposited {amount}, Account balance is ${self.balance:.2f}")

    def viableTranscation(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, your balance is {self.balance}, and withdrawal amount is {amount}")
        
    def withdraw(self, amount):
        try:
            self.viableTranscation(amount)
            self.balance -= amount
            print("Withdrawal Complete\n")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdrawal Interrupted: {error}")

    def transfer(self, recipient,amount):
        try:
            self.viableTranscation(amount)
            self.balance -= amount
            recipient.deposit(amount, False)
            print("Transfer complete")
            self.getBalance()
        except BalanceException as err1:
            print(f"Transfer Interrupted: {err1}")

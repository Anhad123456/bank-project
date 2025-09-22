class BalanceException(Exception):
    pass

class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account created \n Name : {name} \n Balance : ${balance}")

    def getBalance(self):
        print(f"Account balance is ${self.balance:.2f}")
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
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
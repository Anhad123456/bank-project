class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account created \n Name : {name} \n Balance : ${balance}")

    def getBalance(self):
        print(f"Account balance is ${self.balance:.2f}")
        return self.balance
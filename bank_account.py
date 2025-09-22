class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account created \n Name : {name} \n Balance : {balance}")
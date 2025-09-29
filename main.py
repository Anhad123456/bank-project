from bank_account import BankAccount

anhad = BankAccount("Anhad", 200.0)

bob = BankAccount("Bob", 500.0)


# anhad.withdraw(100.0)

# bob.withdraw(600.0)

anhad.deposit(200)

anhad.transfer(bob, 1000)

bob.getBalance()

class Bank_Account:

    def __init__(self, accountNumber, customerName, balance):
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.balance = balance
    
    def deposit(self, deposit):
        print("Depositing", deposit, "\n")
        self.balance += deposit
    
    def withdraw(self, withdraw):
        print("Withdrawing:  ", withdraw)
        if self.balance >= withdraw:
            self.balance -= withdraw
            print("Withdrawal Successful\n")
        else:
            print("Withdrawal Unsuccessful\n")

    def __str__(self):
        return f"Account Number   : {self.accountNumber}\nCustomer Name    : {self.customerName}\nAccount Balance  : $" + format(self.balance, ",.2f")
    
account1 = Bank_Account(487512, "Dave", 2300.00)
print("Opening Balance\n", account1, "\n", sep='')
account1.withdraw(300.0)
account1.withdraw(3000.0)
account1.deposit(253.29)
print("Closing Balance\n", account1, sep='')
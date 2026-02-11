class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance 
        
    def deposite(self,amount):
        if amount>0:
            self.balance += amount
            print(f"₹{amount} deposited successfuly") 
        else:
            print("Deposite amount must be positive.") 
            
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        elif amount > 0:
            self.balance-= amount
            print (f"₹{amount} withdraw successfully.")
        else:
            print("Insufficient balance.")
            
    def check_balance(self):
        print(f"Current Balance:₹{self.balance}")
    
account = BankAccount(200,1000)
account.withdraw(10)
account.deposite(69)
account.check_balance() 
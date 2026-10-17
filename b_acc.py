class BalException(Exception):
    pass
class BankAccount:
    def __init__(self, name, balance):
        self.name= name
        self.balance = balance
        print(f"{self.name} has balance of Rs.{balance} in his account.\n")
    def checkBal(self):
        print(f"{self.name} : {self.balance}\n")
    def deposit(self, amt):
        self.balance += amt
        print(f"{amt} deposited\n")
    def wd_valid(self,amt):
        if(amt> self.balance):
            raise BalException("Balance not enough")
    def withdraw(self,amt):
        try:
            self.wd_valid(amt)
            self.balance -= amt
            print(f"Current balance is {self.balance}\n")
        except BalException as error:
            print(f"Not enough balance\n")
    def transfer(self,amt,account):
        try:
            self.wd_valid(amt)
            self.balance -=amt
            account.balance +=amt
            print(f"Transferred {amt} from {self.name} : {self.balance} to {account.name} : {account.balance}")
        except BalException as error:
            print(f"Not enough money to transfer")
class SavingsAccount(BankAccount):
    def __init__(self,name,balance,fee):
        super().__init__(name,balance)
        self.fee=fee
    def withdraw(self,amt):
            try:
                self.wd_valid(amt*(self.fee))
                self.balance -= (amt*(self.fee))
                print(f"Current balance is {self.balance}\n")
            except BalException as error:
                print(f"Not enough balance\n")

class Bank:
    accno:int
    name:str
    ifsccode:str
    branch:str
    ac_type:str
    balance:int
    bank_name:str

    def create(self,accno,name,ifsccode,branch,ac_type,balance,bank_name):
        self.accno=accno
        self.name=name
        self.ifsccode=ifsccode
        self.branch=branch
        self.ac_type=ac_type
        self.balance=balance
        self.bank_name=bank_name

    def deposit(self,amount):
        self.balance=amount
        print(f"your {self.bank_name} has been credited with amount {amount} aval bal {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance transaction declined")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debitted with amount{amount} avail balance {self.balance}")
    
    def get_balance(self):
        print(f"your aval bal {self.balance}")

obj=Bank()
obj.create(1000,"ajith","sbkc001","nenmara","savings",34000,"sbi")
obj.deposit(5000)
obj.withdraw(100)
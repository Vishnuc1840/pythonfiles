from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def fund_transfer(self):
        pass

    @abstractmethod
    def bal_enq(self):
        pass

    @abstractmethod
    def transaction_history(self):
        pass 

class Gpay(Bank):

    def fund_transfer(self):
        print("Gpay fund transfer")

    def bal_enq(self):
        print("gpay balance enqury")

    def transaction_history(self):
        print("gpay transaction history")

    def gift_card(self):
        print("gpay gift_card")


obj=Gpay()
obj.fund_transfer()
obj.transaction_history()
obj.gift_card()
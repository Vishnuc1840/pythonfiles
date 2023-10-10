class Mobile:
    def mob(self):
        print("oneplus")
    def car(self):
        print("bmw")
    def bike(self):
        print("h2r")


class Child(Mobile):
    def bike(self):
        print("pulsar")

obj=Child()
obj.mob()
obj.car()
obj.bike()



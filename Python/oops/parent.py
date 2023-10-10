class Parent:

    phone="samsung55"
    bike="harley"

    def mobile(self):
        print(self.mobile)
    def vehicle(self):
        print(self.bike)

class Child(Parent):
    pass
obj=Child()
obj.mobile()

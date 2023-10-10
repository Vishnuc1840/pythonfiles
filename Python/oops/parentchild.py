class Parent:

    props=["passion pro,swift"]

    def get_properties(self):
        return self.props

class Child(Parent):

    def get_properties(self):
       self.p=super().get_properties()
       self.p.append("hunter")
       return self.p

ch=Child()
print(ch.get_properties())


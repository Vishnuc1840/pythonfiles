from abc import ABC,abstractmethod

class Bike:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def breake(self):
        pass

class Hunter(Bike):

    def start(self):
        print("Hunter starts")

    def accelerate(self):
        print("Hunter accelerate")

    def stop(self):
        print("Hunter stops")

obj=Hunter()
obj.start()
obj.accelerate()
obj.stop()


class Car:
    def start(self):
        print("key_start")

    def braking_system(self):
        print("drum_brake")

    def transmission(self):
        print("manual")

class Ambasidor(Car):
    pass

class Maruthi(Car):
    def braking_system(self):
        print("disc_brake")

class Audi(Car):
    def start(self):
        print("button_start")
    def braking_system(self):
        print("abs")
    def transmission(self):
        print("automatic transmission")

aobj=Ambasidor()

mobj=Maruthi()
mobj.braking_system()

auobj=Audi()
auobj.start()
auobj.braking_system()
auobj.transmission()
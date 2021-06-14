class Car(object):
    def __init__(self, model, colour, company, speed_limit):
        self.model = model
        self.colour = colour
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def acceleration(self):
        print("accelerating")

audi = Car("A6", "red", "Honda", 40)
print(audi.start())
print(audi.stop())
print(audi.acceleration())
print(audi.colour)    
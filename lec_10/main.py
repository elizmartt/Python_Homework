from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, name, model, year, engine):
        super().__init__(name, model, year)
        self.engine= engine

    def display_info(self):
        return f"{super().display_info()} with {self.engine} engne"

    def move(self):
        return f"Car {self.display_info()} is moving"

class Plane(Vehicle):
    def __init__(self, name, model, year, passengers_number):
        super().__init__(name, model, year)
        self.passengers_number = passengers_number

    def display_info(self):
        return f"{super().display_info()} with a passenger number of {self.passengers_number}"

    def move(self):
        return f"The plane {self.display_info()} is moving"

class Boat(Vehicle):
    def __init__(self, name, model, year, type_of_boat):
        super().__init__(name, model, year)
        self.type_of_boat = type_of_boat

    def display_info(self):
        return f"{super().display_info()} which is a {self.type_of_boat} boat"

    def move(self):
        return f"The boat {self.display_info()} is moving"

class RaceCar(Car):
    def __init__(self, name, model, year, engine,speed):
        super().__init__(name, model, year,engine)
        self.speed = speed
    def display_info(self):
        return f"{super().display_info()} with speed of {self.speed} is Formula1 car)"
    def move(self):
        return f"The Race car {self.display_info()} is moving"

car = Car("Infinity", "qx", 2010, 5.6)
plane = Plane("Boing", "F-150", 2005, 300)
boat = Boat("Titanic", "  ", 1912, "cruiser")
racecar=RaceCar("Ferrari","312 B3-74",1974,"3.0L V12","310 km/h (193 mph")

print(car.move())
print(plane.move())
print(boat.move())
print(racecar.move())

print(car.display_info())
print(plane.display_info())
print(boat.display_info())
print(racecar.display_info())
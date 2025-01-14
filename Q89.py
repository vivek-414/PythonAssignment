class Car:
    def __init__(self, make="Unknown", model="Unknown", year=2022):
        self.make = make
        self.model = model
        self.year = year

car = Car()
print(f"Car: {car.make} {car.model} ({car.year})")

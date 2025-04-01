class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_details(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand)
        self.model = model
        self.seats = seats

    def show_details(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, engine_capacity):
        super().__init__(brand)
        self.engine_capacity = engine_capacity

    def show_details(self):
        print(f"Bike Brand: {self.brand}, Engine Capacity: {self.engine_capacity} CC")


car1 = Car("Toyota", "Corolla", 5)
bike1 = Bike("Yamaha", 150)

car1.show_details()
bike1.show_details()
print("1/23/SET/BCS/358")

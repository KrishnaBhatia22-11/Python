class Car:
    def __init__(self, brand, color):

        self.brand = brand
        self.color = color
        print(f"Car {self.brand} of color {self.color} is created.")

    def display_details(self):

        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")

    def __del__(self):

        print(f"Car {self.brand} is being deleted.")

car1 = Car("Toyota", "Red")
car1.display_details()
del car1
print("1/23/SET/BCS/358")

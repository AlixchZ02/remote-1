# cars.py
import random

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    def get_random_model_year(self):
        return random.randint(2000, 2023)

# Creating an instance of Car
my_car = Car(brand="Toyota", model="Camry", year=2022)

# Displaying car information
my_car.display_info()

# Getting and displaying a random model year
random_year = my_car.get_random_model_year()
print(f"Random Model Year: {random_year}")


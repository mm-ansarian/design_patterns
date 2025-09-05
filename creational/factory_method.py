'''
In this module, we are going to be using the Factory Method Design Pattern in our code.
This is going to be a very simple example to show using the Factory Method Design Pattern more clear.

The Factory Method Design Pattern provides an interface for creating objects in a superclass 
but allows subclasses to alter the type of objects that will be created.

You can read more about this Design Pattern from this url: 
https://www.geeksforgeeks.org/factory-method-for-designing-pattern/
'''


# Importing `ABC` and `abstractmethod` to create abstract classes and methods.
from abc import ABC, abstractmethod


# Defining an abstract class that acts as an interface for all vehicle classes.
class Vehicle(ABC):
    @abstractmethod
    def order(self):  # Abstract method (to be implemented in subclasses). It does nothing here.
        pass


# Concrete class representing a Car, inheriting from `Vehicle`.
class Car(Vehicle):
    def order(self):
        return 'Your Mercedes Benz car is ready!'
    

# Concrete class representing a Truck, inheriting from `Vehicle`.
class Truck(Vehicle):
    def order(self):
        return 'Your Mercedes Benz truck is ready!'
    

# Concrete class representing a Bus, inheriting from `Vehicle`.
class Bus(Vehicle):
    def order(self):
        return 'Your Mercedes Benz bus is ready!'
    

# Concrete class representing a Formula 1 car, inheriting from `Vehicle`.
class Formula1(Vehicle):
    def order(self):
        return 'Your Mercedes Benz Formula 1 is ready!'
    

# Concrete class representing a Bicycle, inheriting from `Vehicle`.
class Bicycle(Vehicle):
    def order(self):
        return 'Your Mercedes Benz bicycle is ready!'
    

# Abstract Factory class that declares the method for creating vehicles.
class VehicleFactory(ABC):
    @abstractmethod
    def create_instance(self) -> Vehicle:  # Abstract method to be implemented in subclasses.
        pass


# Factory class for creating Car objects.
class CarFactory(VehicleFactory):
    def create_instance(self) -> Vehicle:
        return Car()


# Factory class for creating Truck objects.
class TruckFactory(VehicleFactory):
    def create_instance(self) -> Vehicle:
        return Truck()


# Factory class for creating Bus objects.
class BusFactory(VehicleFactory):
    def create_instance(self) -> Vehicle:
        return Bus()


# Factory class for creating Formula 1 objects.
class Formula1Factory(VehicleFactory):
    def create_instance(self) -> Vehicle:
        return Formula1()


# Factory class for creating Bicycle objects.
class BicycleFactory(VehicleFactory):
    def create_instance(self) -> Vehicle:
        return Bicycle()


# Function to run the program.
def run_code():
    # Dictionary mapping user input strings to factory instances.
    factory_dict = {
        'car': CarFactory(),
        'truck': TruckFactory(),
        'bus': BusFactory(),
        'f1': Formula1Factory(),
        'bike': BicycleFactory(),
    }

    # Taking input from the user. 
    vehicle_input = input('What vehicle do you need? ').lower()

    # Validating input and creating the corresponding object.
    try:
        instance = factory_dict.get(vehicle_input)
        result = instance.create_instance()
    except:
        return '!! Invalid Input !!'

    # Returning the result of the `order` method (e.g., "Your Mercedes Benz ... is ready!").
    return result.order()


# Running the program in the main module.
if __name__ == '__main__':
    print(run_code())

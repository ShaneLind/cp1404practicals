"""
CP1404 Practical
"""
# from car import Car
from taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)

my_taxi.start_fare()
my_taxi.drive(40)
print(my_taxi.__str__())
print(f"Current fare = ${my_taxi.get_fare()}")

my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi.__str__())
print(f"Current fare = ${my_taxi.get_fare()}")
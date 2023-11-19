"""
CP1404 Practical
SilverServiceTaxi test file
"""

from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)
my_taxi2 = SilverServiceTaxi(name="Vehicle", fuel=200, fanciness=2)

my_taxi.start_fare()
my_taxi.drive(0)
print(my_taxi.__str__())
print(f"Current fare = ${my_taxi.get_fare():.2f}")

my_taxi2.start_fare()
my_taxi2.drive(18)
print(my_taxi2.__str__())
print(f"Current fare = ${my_taxi2.get_fare():.2f}")



"""
CP1404 Practical
UnreliableCar test file
"""
from unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar(name="U Car 1", fuel=100, reliability=76.5)

print(f"{my_unreliable_car}")
my_unreliable_car.drive(60)
print(f"{my_unreliable_car}")

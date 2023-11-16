"""
CP1404 Practical
SilverServiceTaxi class file
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.current_fare_distance = 0
        self.number_of_fares = 1

    def get_fare(self):
        """Return the price for the taxi trip like parent class,
        but adds an extra charge for each now fare."""
        current_fare = super().get_fare() + (self.flagfall * self.number_of_fares)
        self.number_of_fares += 1
        return current_fare

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km "
                f"plus a flagfall of ${self.flagfall * self.number_of_fares}")

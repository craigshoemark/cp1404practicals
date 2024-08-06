"""
Class: SilverServiceTaxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi, inherits from Taxi, with addition fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string like Taxi with addition of fanciness and flagfall."""
        return (f"{super().__str__()}, fanciness={self.fanciness}, price per km=${self.price_per_km:.2f}/km,"
                f" plus flagfall of ${self.flagfall:.2f}")

    def get_fare(self):
        """Get fare with additional flagfall fee"""
        return super().get_fare() + self.flagfall

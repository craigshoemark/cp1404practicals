"""
Objects: SilverServiceTaxi
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

# Silver taxi
silver_taxi = SilverServiceTaxi(name="Silver", fuel=100, fanciness=2.0)
silver_taxi.drive(10)
print(silver_taxi)
print("Total fare $", silver_taxi.get_fare())
print()

# Hummer
hummer = SilverServiceTaxi(name="Hummer", fuel=100, fanciness=4.0)
print(hummer)
print("Total fare $", hummer.get_fare())
print()

# Test SilverServiceTaxi using assert
silver_taxi_test = SilverServiceTaxi(name="Silver taxi test", fuel=100, fanciness=2.0)
silver_taxi_test.drive(18)
assert silver_taxi_test.get_fare() == 48.78, f"Expected 48.78, got ${silver_taxi_test.get_fare()}"
print(silver_taxi_test)
print("Total fare $", silver_taxi_test.get_fare())
print("Test successful")

"""
Object: UnreliableCar
"""
from prac_09.unreliable_car import UnreliableCar

old_car = UnreliableCar(name="Herby", fuel=100, reliability=50.0)

old_car.drive(10)
print(old_car)

class Vehicle:
    vehicle_type = "none"
class Car:
    price = 1000000
    def horse_powers(self):
        powers = 100
        return powers

class Nissan(Vehicle, Car):
    vehicle_type = 'sedan'
    price = 2000000
    def horse_powers(self):
        powers = 200
        return powers


vehicle = Vehicle()
print(vehicle.vehicle_type)
car = Car()
print(car.price, car.horse_powers())
nissan = Nissan()
print(nissan.vehicle_type, nissan.price, nissan.horse_powers())
class Car:
    price = 1000000
    def horse_powers(self):
        powers = 100
        return powers

class Nissan(Car):
    price = 2000000
    def horse_powers(self):
        powers = 200
        return powers

class Kia(Car):
    price = 1500000
    def horse_powers(self):
        powers = 150
        return powers

car = Car()
print('Стоимость:', car.price, 'Мощность:', car.horse_powers())
nissan = Nissan()
print('Стоимость:', nissan.price, 'Мощность:', nissan.horse_powers())
kia = Kia()
print('Стоимость:', kia.price, 'Мощность:', kia.horse_powers())



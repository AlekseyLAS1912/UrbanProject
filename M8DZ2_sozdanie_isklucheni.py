class InvalidDataException(Exception):
    def __init__(self, speed, minspeed, maxspeed):
        self.speed = speed
        self.min_speed = minspeed
        self.max_speed = maxspeed
    def __str__(self):
        return (f"Недопустимое значение скорости: {self.speed}!"
                f"Рекомендуемая скорость: от {self.min_speed} до {self.max_speed}.")
class ProcessingException(Exception):
    def __init__(self, used):
        self.used_road = used
    def __str__(self):
        return print('Дорога закрыта!')

class Road:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        minspeed = 20
        maxspeed = 90
        if minspeed < speed < maxspeed:
            self.speed = speed
        else:
            raise InvalidDataException(speed, minspeed, maxspeed)

    def speed_info(self):
        print(f'На дороге {self.name} допустимая скрость: {self.speed}')
class Used(Road):
    def __init__(self, use):
        self.used = use
        if use == 0:
            self.used = use
        else:
            raise ProcessingException(use)
    def road_info(self):
        print('Проезжайте!')

try:
    road = Road('дорога1', 70)
    road.speed_info()
    used = Used(0)
    used.road_info()

    road = Road('дорога2', 50)
    road.speed_info()
    used = Used(0)
    used.road_info()

except InvalidDataException as ide:
    print(ide)
except ProcessingException as pe:
    print(pe)

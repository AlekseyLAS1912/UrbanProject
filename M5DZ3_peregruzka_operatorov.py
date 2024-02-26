class Building:

    def __init__(self, floor = None, type = None):
        self.numberOfFloor = floor
        self.buildingType = type

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloor == other.numberOfFloor

building1 = Building(12, 'Дом')
building2 = Building(12, 'Школа')

if Building.__eq__(self = building1, other = building2):
    print('Одинаково')
else:
    print('Отличаются')








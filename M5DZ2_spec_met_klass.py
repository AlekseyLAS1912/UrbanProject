class House:
    def __init__(self):
        self.numberOfFloor = 0

    def setNewNumberOfFloor(self, floor):
        self.numberOfFloor = floor

house = House()
house.setNewNumberOfFloor(100)
print('Текущий этаж равен', house.numberOfFloor)
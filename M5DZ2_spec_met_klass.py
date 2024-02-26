class House:
    def __init__(self):
        self.numberOfFloor = 0

    def setNewNumberOfFloor(self, floor):
        self.numberOfFloor = floor
        print('Текущий этаж равен', house.numberOfFloor)

house = House()
house.setNewNumberOfFloor(100)

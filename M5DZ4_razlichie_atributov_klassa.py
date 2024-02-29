from random import randint
class Building:
    total = 0
    def __init__(self):
        Building.total += 1

objects = []
objects_size = randint(40, 40)
while len(objects) < objects_size:
    new_building = Building()
    objects.append(new_building)

print(Building.total)
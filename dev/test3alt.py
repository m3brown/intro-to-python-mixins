class Building(object):
    knock_first = False
    greet_receptionist = False

    def unlock(self):
        if knock_first:
            print("knock knock")

        print("unlocking!")

        if greet_receptionist:
            print("good morning!")

class ExcellaHQ(Building):
    greet_receptionist = True

class ParentsHouse(Building):
    knock_first = True

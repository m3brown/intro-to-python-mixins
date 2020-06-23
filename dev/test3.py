class Building(object):
    def unlock(self):
        print("unlocking!")

class KnockFirstMixin(object):
    def unlock(self):
        print("knock knock")
        super().unlock()

class GreetReceptionistMixin(object):
    def unlock(self):
        super().unlock()
        print("good morning!")

class ExcellaHQ(GreetReceptionistMixin, Building):
    pass

class ParentsHouse(KnockFirstMixin, Building):
    pass

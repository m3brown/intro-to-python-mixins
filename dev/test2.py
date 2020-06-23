class Building(object):
    lock = MetalKey()

    def unlock(self):
        self.lock.attempt_unlock()

class KeyCardMixin(object):
    lock = KeyCard()

class ExcellaHQ(KeyCardMixin, Building):
    pass

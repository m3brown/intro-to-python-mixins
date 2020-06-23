class Residence:
    def __init__(self):
        print("I am a residence")

class HighRise:
    def __init__(self):
        print("I am a high rise")
        super().__init__()

class ApartmentBuilding(HighRise, Residence):
    def __init__(self):
        print("I am an apartment")
        super().__init__()

ApartmentBuilding()

# Output:
# I am an apartment
# I am a high rise
# I am a residence

class DoubleMixin(object):
    ratio = 2

class HalfMixin(object):
    ratio = .5

class Recipe(object):
    ratio = 1

    def __init__(self):
        print(f"I need {self.ratio} servings")

class LargeRecipe(DoubleMixin, Recipe):
    pass

Recipe()
LargeRecipe()

# Output:
# I need 1 servings
# I need 2 servings

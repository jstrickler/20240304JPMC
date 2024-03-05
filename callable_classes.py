
class Spam:
    def __init__(self, animal):
        self.animal = animal

    def foo(self):
        print(self.animal.upper())

s = Spam('wombat')
s.foo()

class Ham:
    def __init__(self, animal):
        self.animal = animal

    def __call__(self):
        print(self.animal.upper())

h = Ham('badger')
h()

import random

class Witch:

    def __init__(self, name):
        self.name = name
        self.beaten = False

    def __str__(self):
        return 'Name: ' + self.name

    def fight(self, n):
        if random.random() < n * 0.01:
            self.beaten = True
            print('You have beaten the wtich!')
        else:
            print('You have been beaten by the witch!')

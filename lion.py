class Lion:

    def __init__(self, name):
        self.name = name
        self.spoken = False

    def __str__(self):
        return 'Name: ' + self.name

    def talk(self):
        self.spoken = True
        print('You have spoken with the lion!')

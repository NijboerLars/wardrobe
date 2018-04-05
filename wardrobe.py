class Wardrobe:

    def __init__(self, material, name):
        self.name = name
        if material.lower() == 'glass' or material.lower() == 'wood' or material.lower() == 'carbon fiber':
            self.material = material
        else:
            print('Only the following materials are accepted: Wood, carbon fiber or glass.')
        self.open = False
        self.inside = False
        self.intact = True

    def __str__(self):
        return 'Name: ' + self.name + ', Material: ' + self.material

    def open(self):
        if self.intact:
            if self.open == False:
                self.open = True
            else:
                print('Wardrobe is already open.')
        else:
            print('Wardrobe has been broken.')

    def close(self):
        if self.intact:
            if self.open:
                self.open = False
            else:
                print('Wardrobe is already closed.')
        else:
            print('Wardrobe has been broken.')

    def get_in(self):
        if self.intact:
            if self.open:
                if self.inside == False:
                    self.inside = True
                else:
                    print('You are already in the wardrobe.')
            else:
                print('Wardrobe needs to be opened first.')
        else:
            print('Wardrobe has been broken.')

    def get_out(self):
        if self.intact:
            if self.inside:
                self.inside = False
            else:
                print('You are not in the wardrobe.')
        else:
            print('Wardrobe has been broken.')

    def kick(self):
        if self.material.lower() == 'wood':
            print('Wardrobe still intact.')
        if self.material.lower() == 'carbon fiber' or self.material.lower() == 'glass':
            self.intact = False
            print('Wardrobe has been damaged.')


Wardrobe(material = 'wood', name = 'Pax')

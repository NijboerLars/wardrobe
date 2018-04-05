from wardrobe import Wardrobe
import random

materials = ['wood', 'carbon fiber', 'glass']
wardrobe1 = Wardrobe(random.choice(materials), 'Magical Wardrobe')
n = 1
lion = False
while lion == False:
    wardrobe1.kick()
    while wardrobe1.intact == False:
        wardrobe1 = Wardrobe(random.choice(materials), 'Magical Wardrobe')
        wardrobe1.kick()
    wardrobe1.open_wardrobe()
    wardrobe1.get_in()
    if random.random() < 0.01:
        print('You have entered Narnia!')
        if random.random() < n * 0.01:
            print('You have beaten the witch!')
            lion = True
            print('Succes!')
        else:
            print('You got beaten by the witch!')
            n += 1
    wardrobe1.get_out()
    wardrobe1.close_wardrobe()

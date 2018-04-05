from wardrobe import Wardrobe
from witch import Witch
from lion import Lion
import random

materials = ['wood', 'carbon fiber', 'glass']
wardrobe1 = Wardrobe(random.choice(materials), 'Magical Wardrobe')
witch1 = Witch('The Witch')
lion1 = Lion('The Lion')
n = 1
while lion1.spoken == False:
    wardrobe1.kick()
    while wardrobe1.intact == False:
        wardrobe1 = Wardrobe(random.choice(materials), 'Magical Wardrobe')
        wardrobe1.kick()
    wardrobe1.open_wardrobe()
    wardrobe1.get_in()
    if random.random() < 0.01:
        print('You have entered Narnia!')
        witch1.fight(n)
        if witch1.beaten:
            lion1.talk()
        else:
            n += 1
    wardrobe1.get_out()
    wardrobe1.close_wardrobe()

zoo = ('naked mole rat', 'dog', 'monkey', 'lemur', 'python', 'chinchilla', 'goat')

print("Index for lemur: ", zoo.index( 'lemur' ))

[print('There is a {0} in the zoo'.format(animal)) for animal in zoo if animal == 'chinchilla']


import code
code.interact(local=locals())

import random
from enterprise import HikaruSulu as Sulu

sulu = Sulu()
res = sulu.indirect_orbits(0, {}, {'COM': ['B'],
        'B': ['C', 'G'],
        'C': ['D'], 
        'D': ['E', 'I'], 
        'E': ['F', 'J'], 
        'G': ['H'], 
        'J': ['K'], 
        'K': ['L']})


import pytest
from unittest import TestCase
from enterprise import HikaruSulu as Sulu

class Test_Enterprise(TestCase):
    def test_objects(self):
        sulu = Sulu()
        res = sulu.objects(
        ["COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L"])
        self.assertEqual(res, {'COM': ['B'],
        'B': ['C', 'G'],
        'C': ['D'], 
        'D': ['E', 'I'], 
        'E': ['F', 'J'], 
        'G': ['H'], 
        'J': ['K'], 
        'K': ['L']})

    def test_direct_orbits(self):
        sulu = Sulu()
        res = sulu.direct_orbits({'COM': ['B'],
        'B': ['C', 'G'],
        'C': ['D'], 
        'D': ['E', 'I'], 
        'E': ['F', 'J'], 
        'G': ['H'], 
        'J': ['K'], 
        'K': ['L']})
        self.assertEqual(res, 11)
    
    def test_indirect_orbits(self):
        sulu = Sulu()
        res = 0 
        orbits = {'COM': ['B'],
        'B': ['C', 'G'],
        'C': ['D'], 
        'D': ['E', 'I'], 
        'E': ['F', 'J'], 
        'G': ['H'], 
        'J': ['K'], 
        'K': ['L']}
        for _, orbs in orbits.items():
            for key in orbs:
                res += sulu.indirect_orbits(0, key, {}, orbits)
        
        self.assertEqual(res, 31)

    
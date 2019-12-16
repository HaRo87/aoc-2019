import pytest
import random
from unittest import TestCase
from enterprise import MontgomeryScott as Scotty

class Test_Enterprise(TestCase):
    def test_translate(self):
        scotty = Scotty(input=1, pset=0)
        res = scotty.translate('3,0,4,0,99')
        self.assertEqual(res, [3, 0, 4, 0, 99])

    def test_case_one(self):
        result = {}
        finish = False
        scotty = Scotty(input=0, pset=0)
        trans = scotty.translate('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')
        while not finish:
            if len(result) >= 120:
                finish = True
            combs = []
            while len(combs) < 5:
                setting = random.randint(0,4)
                if setting not in combs:
                    combs.append(setting)
                continue
            if combs in result.values():
                continue
            res = 0
            for p in combs: 
                scotty = Scotty(input=res, pset=p)
                res = scotty.execute(trans.copy())[0]
            result[res] = combs    
        
        self.assertEqual(result[max(result.keys())], [4, 3, 2, 1, 0])
        self.assertEqual(max(result.keys()), 43210)

    def test_case_two(self):
        result = {}
        finish = False
        scotty = Scotty(input=0, pset=0)
        trans = scotty.translate('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0')
        while not finish:
            if len(result) >= 120:
                finish = True
            combs = []
            while len(combs) < 5:
                setting = random.randint(0,4)
                if setting not in combs:
                    combs.append(setting)
                continue
            if combs in result.values():
                continue
            res = 0
            for p in combs: 
                scotty = Scotty(input=res, pset=p)
                res = scotty.execute(trans.copy())[0]
            result[res] = combs    
        
        self.assertEqual(result[max(result.keys())], [0, 1, 2, 3, 4])
        self.assertEqual(max(result.keys()), 54321)

    def test_case_three(self):
        result = {}
        finish = False
        scotty = Scotty(input=0, pset=0)
        trans = scotty.translate('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0')
        while not finish:
            if len(result) >= 120:
                finish = True
            combs = []
            while len(combs) < 5:
                setting = random.randint(0,4)
                if setting not in combs:
                    combs.append(setting)
                continue
            if combs in result.values():
                continue
            res = 0
            for p in combs: 
                scotty = Scotty(input=res, pset=p)
                res = scotty.execute(trans.copy())[0]
            result[res] = combs    
        
        self.assertEqual(result[max(result.keys())], [1, 0, 4, 3, 2])
        self.assertEqual(max(result.keys()), 65210)
    
    
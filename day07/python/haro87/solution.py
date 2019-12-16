import random
import os
from enterprise import MontgomeryScott as Scotty

cwd = os.getcwd()
ifile = cwd + "/input.txt"

with open(ifile, "r") as commands:
    #Part one
    scotty = Scotty(input=0, pset=0)
    trans = scotty.translate(commands.read())
    
    result = {}
    finish = False
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

    print("Scotty says the solution for part one is: {0}".format(max(result.keys())))

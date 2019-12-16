import collections

class HikaruSulu:

    def orbitmaps(self, input):
        return input.splitlines()
    
    def objects(self, orbitmap):
        objects = {}
        for orbit in orbitmap:
            m = orbit.split(")")
            obj = m[0]
            orb = m[1]
            if obj not in objects:
                objects[obj] = [orb]
            else:
                objects[obj].append(orb)
        return objects

    def direct_orbits(self, objects):
        count = 0
        for _, orbs in objects.items():
            count += len(orbs)
        return count

    def indirect_orbits(self, ocount, cobj, orbits, objects):
        if not orbits == objects:
            for obj, orbs in objects.items():
                if cobj in orbs:
                    ocount +=  1 * len(orbs)
                    orbits[obj] = orbs
                    self.indirect_orbits(ocount=ocount, cobj=obj, orbits=orbits, objects=objects)
                if obj == "COM":
                    if "COM" not in orbits:
                        orbits[obj] = orbs
                        ocount += 1
        return ocount
            
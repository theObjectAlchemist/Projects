import sys
sys.path.insert(0, 'C:/DzasterusTesting/Team/CuleBase/MemoryModules/DataTypes')

from atom import Atom

class AtomWriter(object):

    def WriteAtomToFile(self, elem: Atom)->None:
        try:
            testFile = open(elem.IDType().Get('Name')+'.txt', 'r')
            testFile.close()
        except (IOError):
            auxFile = open(elem.IDType().Get('Name')+'.txt', 'w')
            auxFile.write(str(elem))
            auxFile.close()

import sys
sys.path.insert(0, 'C:/DzasterusTesting/Team/CuleBase/MemoryModules/DataTypes')
##CHANGE THE ABOVE PATH TO WHERE atom.py RESIDES IN ORDER FOR THE FOLLOWING
##IMPORT STATEMENT TO WORK
from atom import Atom

class CannotFindAtomFile(Exception):
    pass


class AtomWriter(object):

    def WriteAtomToFile(self, elem: Atom)->None:
        try:
            testFile = open(elem.IDType().Get('Name')+'.txt', 'r')
            testFile.close()
        except (IOError):
            auxFile = open(elem.IDType().Get('Name')+'.txt', 'w')
            auxFile.write(str(elem))
            auxFile.close()


    def ReadAtomFromFile(self, elem: str)->Atom:
        try:
            auxFile = open(elem+'.txt', 'r')
            ###OPERATIONS GO HERE
            auxFile.close()
        except (IOError):
            raise CannotFindAtomFile()

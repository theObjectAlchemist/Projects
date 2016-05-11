import sys
sys.path.insert(0, 'C:/DzasterusTesting/Team/CuleBase/MemoryModules/DataTypes')
from atom import Atom
from atomID import AtomID
from atomOTHER import AtomOTHER



class AtomGenerator (object):
    """Object which protects the Atom object by adding a layer which
        allows for edit and creation"""

    def __init__(self, atom = None):
        self._ID = None
        self._OTHER = None
        if type(atom) != type(None): #change this to check for type of input
            self._ID = atom.IDTYPE()
            self._OTHER = atom.OTHERType()


    def GetAtomIDinfo(self)->list:
        """returns atomID info GetAll() function of AtomID instance"""
        return self._ID.GetAll()


    def PromptUserForID(self, need = [None]*4):
        """need should a 4 element list of [str, str, int, float]
            whatever is not none in the order of name, abr, anum, amas
            then prompt user for the required field"""
        needList = ['Name', 'Abbreviation', 'Atomic Number', 'Atomic Mass']
        returnList = need[:]

        for i in range(0, len(needList)):
            if need[i] == None:
                aux = input('{}: '.format(needList[i]))
                if i == 2:
                    aux = int(aux)
                elif i == 3:
                    aux = float(aux)
                returnList[i] = aux
        return returnList


    def PromptUserForOTHER(self):
        pass #different mechanics since optional

    def SetAtomID(self, name:str, abr:str, anum:int, amass:float)->None:
        self._ID = AtomID(name, abr, anum, amass)

    def SetAtomIDSpecific(self, attr:str, val):
        self._ID.Set(attr, val)

    def SetAtomOTHER(self, attr = {}):
        self._OTHER = AtomOTHER(attr)

    def SetAtomOTHERSpecific(self, attr:str, val):
        self._OTHER.Set(attr, val)


    def GenerateAtom(self)->Atom:
        return Atom(self._ID, self._OTHER)
    

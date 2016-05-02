from atomID import AtomID
from atomOTHER import AtomOTHER

class Atom(object):

    def __init__(self, ID:AtomID, OTHER = None)->None:
        self._ID = ID

        if type(OTHER) != type(AtomOTHER()):
            OTHER = AtomOTHER()

        self._OTHER = OTHER

    def IDType(self):
        return self._ID

    def OTHERType(self):
        return self._OTHER

    def __str__(self)->str:
        aux = str(self._ID)
        if not self.OTHERType().IsEmpty():
            aux += str(self._OTHER)
        return aux
        

from moleculeCOMP import MoleculeCOMP

class MoleculeID(object):

    def __init__(self, name:str, abbr: str, comp:MoleculeCOMP, mmass:float):
        self._attr = {'Name': name, 'Abbreviation': abbr,
                      'Composition':comp, 'Atomic Mass': mmass}



    def Get(self, attr:str)->object:
    """returns the value of the attribute in the dictionary of attributes"""
        try:
            return self._attr[attr]
        except (KeyError):
            return None

    def __str__(self):
        aux = 'IDENTITY\nName: {}\nAbbreviation: {}\nComposition: {}\nAtomic Mass: {}'.format(
            self._attr['Name'], self._attr['Abbreviation'], self._attr['Composition'], self._attr['Atomic Mass'])
        return aux
